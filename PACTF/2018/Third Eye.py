from binascii import *
with open("something", "r") as f:
	string = f.read()
printables = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
stuff = []
for i in string:
	stuff.append(i)
collection = []
for i in stuff:
	if i == '\x8b':
		collection.append(0)
	if i == '\x8c':
		collection.append(1)
print(collection)

words = ""
word = ""
for i in range(len(collection)):
	if i % 8 == 7:
		word += str(collection[i])
		words += unhexlify(hex(int(word,2))[2:])
		print(word)
		word = ""
	else:
		#print(str(collection[i]))
		word += str(collection[i])
print(words)
