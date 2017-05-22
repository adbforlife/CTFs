from base64 import *
file = open("/Users/ADB/Desktop/fb26f2cf8d244f2b1177fd9dc67e977b3d2028f3_encrypted_flag.txt", "r")
base64String = file.readlines()
base64String = [x.strip() for x in base64String]
asciiString = ""
for i in base64String:
    asciiString += i
asciiString = b64decode(asciiString)
asciiString += "="
asciiString = b64decode(asciiString)
asciiString += "="
asciiString = b64decode(asciiString)
asciiString += "=="
asciiString = b64decode(asciiString)
asciiString += "=="
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
print(asciiString)
print(len(asciiString))
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
asciiString = b64decode(asciiString)
print(asciiString)
print(len(asciiString))
file.close()
