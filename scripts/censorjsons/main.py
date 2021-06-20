# id like to not require that in the future
from _secrets import *

to_replace_key = {
	("password",): "--BLANKED-- (password)",
	("trust", "token"): "--BLANKED-- (token)",
	("remote_ident",): "--BLANKED-- (device name)",
	("local_ident",): "--BLANKED-- (email)",
	("params", "token"): "--BLANKED-- (firebase token)",
	("hash",): "--BLANKED-- (hash [nonce_key + salt + token])",
	("salt",): "--BLANKED-- (salt)",
	("nonce_id",): "--BLANKED-- (nonce_id)",
	("nonce", "id"): "--BLANKED-- (nonce_id)",
	("nonce", "key"): "--BLANKED-- (nonce_key)",
	(int, "login"): "--BLANKED-- (group email)",
	(int, "name_hr"): "--BLANKED-- (group name)",
	("session_id",): "--BLANKED-- (session_id)",
	("miniature", "data"): "--BLANKED-- (profile picture in base64)",
	("date",): 0,
	("time",): 0,
	("iso8601",): "--BLANKED-- (time in iso8601)",
	("usage",): 0,
	("free",): 0,
	("limit",): 0,
	("sequence",): 0,
	("updated",): 0,
	("version",): 0
}


def edit_data(data, cur_pos=tuple()):
	return {
		"list": lambda: edit_list(data, cur_pos),
		"dict": lambda: edit_dict(data, cur_pos),
		"str": lambda: edit_string(data, cur_pos)
	}.get(type(data).__name__, lambda: data)()


def edit_list(data_list: list, cur_pos=tuple()):
	new_list = []
	for index, element in enumerate(data_list):
		new_list.append(edit_data(element, cur_pos + (index,)))
	return new_list


def edit_dict(data_dict: dict, cur_pos=tuple()):
	edited_dict = {}
	for key, item in data_dict.items():
		found = False
		for path, to_replace_with in to_replace_key.items():
			# if found:  # i dont think we need that
			# 	break
			if len(cur_pos) >= len(path):
				is_the_case = []
				to_compare_path = (cur_pos + (key,))[-len(path):]
				for index, thing in enumerate(path):
					if type(thing) == type:
						is_the_case.append(type(to_compare_path[index]) == thing)
					else:
						is_the_case.append(to_compare_path[index] == thing)
				if all(is_the_case):
					edited_dict[key] = to_replace_with
					found = True
					break
		if not found:
			edited_dict[key] = edit_data(item, cur_pos + (key,))
	return edited_dict


def edit_string(data_str: str, cur_pos=tuple()):
	return to_replace_str.get(data_str, data_str)


if __name__ == '__main__':
	import json
	import os
	import re
	import sys

	if not has_edited_secrets:
		print("you have not edited the _secrets.py yet. please do that first!")
		sys.exit(1)


	print("WARNING! MAKE SURE YOU HAVE SET YOUR INFORMATION IN THE _secrets.py AND CHECK THE RESULTS AFTERWARDS BEFORE PUBLISHING!")
	os.chdir(path_to_files)

	for file_name in os.listdir():
		with open(file_name, "r", encoding="utf-8") as file:
			json_data = json.load(file)
		final_thing = json.dumps(edit_data(json_data), ensure_ascii=False, indent="\t", sort_keys=False)

		# this is a very bad botch. this has to be changed on the future
		final_thing = re.sub(r'(?<=")[^"]+@[^"]+(?=")', "--BLANKED-- (group email)", final_thing)
		final_thing = re.sub(r'(?<="name_hr": ")(?!--BLANKED--).+(?=")', "--BLANKED-- (group name)", final_thing)

		with open(file_name, "w", encoding="utf-8") as file:
			file.write(final_thing)
		print(file_name, final_thing)
