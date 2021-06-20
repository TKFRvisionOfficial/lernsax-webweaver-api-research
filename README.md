**This project is no way associated with LernSax, WebWeaver, DigiOnline GmbH or Freistaat Sachsen**

# Research on the LernSax/WebWeaver API

## RULES
- Do not DDOS or HACK any platform or person
- Do not use the findings to inflict harm
- Be nice to one another

## OBJECTIVE
Hello, this project is about reverse engineering the LernSax API. It seems that it is build on the same foundation (WebWeaver) as many other school portals around germany. The objectiv is to document the apis this platform uses. Right now we are only working on the Android API (which uses [json_rpc 2.0](https://www.jsonrpc.org/specification)). I have also figured out how the main principles of this api work but have not probarly documented my findings. 


## HOW TO DUMP DATA
For capturing the requests and reponses from the server you can probarly use things like [mitmproxy](https://mitmproxy.org/) but personaly I use a modified version of the lernsax app which logs the requests and reponses via logcat. Because of copyright issues I can't publish the app right now but I am commited to figuring out a way to publish this app (or the modifications) without infringing copyright.


## HOW THIS REPOSITORY WORKS
**[api_dumps](/api_dumps)**<br>
sharing of request/response json dumps created by the app (please censor any personal information and format them properly first)

**[scripts](/scripts)**<br>
is for sharing scripts related to this project or this repository

**[documentation](/documentation)**<br>
sharing markdown documentation of the apis


## SCRIPTS
**[censor_jsons](/scripts/censorjsons)**<br>
A script to censor the personal information of a folder of jsons you dumped. Because I was to lazy to implement argparse you have to edit the _secrets.py before usage. I also botched some of the email replacement with two regex statements which aren't really well though out. Also make sure to check the results before publishing them.
