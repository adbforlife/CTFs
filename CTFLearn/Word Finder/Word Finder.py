import hashlib
file = open("/Users/ADB/Desktop/md5.txt", "r")
strings = file.readlines()
file.close()
for string in strings:
    hexResult = hashlib.md5(string.rstrip() + "6wm3sz4skb").hexdigest()
    if hexResult[0:4] == "e3af" and hexResult[28:32] == "1986":
        print(string)
