from binascii import *

with open("/Users/ADB/Desktop/random", "r") as f:
	string = f.read()

with open("/Users/ADB/Desktop/random2", "w") as f:
	f.write(unhexlify(string[12:]))