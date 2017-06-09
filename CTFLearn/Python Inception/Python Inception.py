from base64 import *
file = open("/Users/ADB/Desktop/PythonInception.py", "r")
strings = file.readlines()
file.close()
flag = ""
for i in strings:
    if "flag +=" in i:
        flag += i[i.index("flag +=") + 9 : -2]
print(b64decode(flag))
