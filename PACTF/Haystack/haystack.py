import json
from base64 import *
with open("/Users/ADB/Desktop/haystack.json") as file:
    data = json.load(file)
list = data["haystack"]
for i in list:
    print(b64decode(i["data"]))
    print(b64decode(i["signature"]))
