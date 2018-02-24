#!/usr/bin/env python3
import binascii
key = "xYwfOVWU"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))

print(str(mystery("easyctf{"), 'utf-8'))

test = "easyctf{"

result3 = "6538c29d4b5fc39a6c28c2a349c38710c3ab3cc2bbc2a4c3a3c2813fc3a0736838c29202c39723c2bf"
result2 = "65389d4b5f9a6c28a3498710c3ab3cc2bbc2a4c3a3c2813fc3a0736838c29202c39723c2bf"
result = []
for i in range(len(result3)):
	if i % 2 == 0:
		result.append(result3[i:i+2])
print(result)
flag = ""
i = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}{_ ?.,<>;:'[]!@#$%^&*()"
while True:
	for c in alphabet:
		if str(mystery(test + c), 'utf-8') in result3:
			test += c
			print(test)

#alphabet = [chr(i) for i in range(10000)]
print(bytes(result[0], "utf-8") == mystery("e")[-2:])
print(mystery("e")[-2:])

while mystery(flag) != result3:
	changed = False
	for c in alphabet:
		#print(result[i])
		#print(mystery(flag + c)[-2:])
		if result[i] == str(mystery(flag + c)[-2:], 'utf-8'):
			flag += c
			i += 1
			changed = True
			break
	if changed == False:
		flag += "?"
		i += 1
	print(flag)

print(result[0])
print(mystery("e")[-2:])