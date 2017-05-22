from binascii import *
from math import *
from base64 import *

file = open("string", "r")
strings = file.readlines()
string = strings[0].rstrip()
print(string)
hexa = hexlify(string)
print(hexa)
hexStrings = []
stra = ""
for i in range(len(hexa)):
    if i % 4 == 0:
        if i > 0:
            hexStrings.append(stra)
        stra = hexa[i]
    else:
        stra += hexa[i]
ints = []
for i in hexStrings:
    ints.append(int(i, 16))
print(ints)
for i in range(len(ints)):
    ints[i] = ints[i] - 50000 + 14
    if ints[i] < 0:
        ints[i] += 192
print(ints)
hexString = ""
for i in ints:
    hexString += hex(i)[2:]
print(unhexlify(hexString))
