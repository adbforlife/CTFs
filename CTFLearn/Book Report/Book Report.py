import math
from base64 import *
from binascii import *

file = open("/Users/ADB/Desktop/CTF/CTFLearn/Book Report/text", "r")
numbers = [13,1,17,3,14,10,18,15,16,13,15,5,5,6,12,8,8,3,2,5,4,10,11,3,1,5,10,1,7,5,6,10,9,4,3,10,15,13]
strings = file.readlines()
for i in range(len(strings)):
    strings[i] = strings[i].rstrip()
result = ""
for i in range(len(numbers)):
    if i % 2 == 0:
        result += strings[numbers[i] - 1][numbers[i + 1] - 1]
print(result)
