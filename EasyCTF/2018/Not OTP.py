from base64 import *
from binascii import *
import math
from scipy import stats

c1 = "38445d4e5311544249005351535f005d5d0c575b5e4f481155504e495740145f4c505c5c0e196044454817564d4e12515a5f4f12465c4a45431245430050154b4d4d415c560c4f54144440415f595845494c125953575513454e11525e484550424941595b5a4b"
c2 = "3343464b415550424b415551454b00405b4553135e5f00455f540c535750464954154a5852505a4b00455f5458004b5f430c575b58550c4e5444545e0056405d5f53101055404155145d5f0053565f59524c54574f46416c5854416e525e11506f485206554e51"
xored = "0b071b0512440400024106001614001d06490448001048540a04421a00105216184516045c493a0f450d4802154e590e195318491e09460b1756111d00065516121e514c034c0e0100191f410c0f071c1b00460e1c11147f1d1a503c0c1654002d01135f0e141a"
print(len(xored))

words = []
with open("/Users/ADB/Desktop/words.txt", "r") as file:
    strings = file.readlines()
    for i in strings:
        words.append(i.rstrip())
for i in words:
    #if len(i) > 4 and i[-1] == 'e' and i[-2] == 'l' and i[-4] == 'b':
    #    print(i)
    if len(i) == 3 and i[0] in "deghijklmnopqrstuvwxyz" and i[1] in "bchijklmnopqrstuvwxy" and i[2] in "oiest":   
        print(i)
    #if len(i) == 4 and i[2] == 't' and i[3] != 'y' and i[3] != 'h':
    #    print(i)
    #if len(i) == 8 and i[-1] == 'g' and i[1] == 'r':
    #    print(i)
#for i in "deghijklmnopqrstuvwxyz":
#    for j in "bchijklmnopqrstuvwxy":
#        for k in "oiest":
#            print(str(i) + str(j) + str(k))

printables = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
weirdCharacters = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
strictPrintables = "0123456789abcdefghijklmnopqrstuvwxyz_}{ "
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
nullHypothesis = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.024, 0.002, 0.02, 0.001]

xored_chars = []
for i in range(len(xored)):
    if i % 2 == 0:
        xored_chars.append(int(hexlify(unhexlify(str(xored[i:i + 2]))), 16))
for i in xored_chars:
    possibles = []
    for c in strictPrintables:
        other_c = chr(ord(c) ^ i)
        if other_c in strictPrintables:
            possibles.append((c, other_c))
    bracket = False
    for j in possibles:
        if '{' in j:
            bracket = True
    #if bracket:
    #    print(possibles)
    #if len(possibles) < 15:
    #    print(possibles)
print(xored_chars)

for i in "0123456789abcdefghijklmnopqrstuvwxyz":
    print(ord(i) ^ ord(' '))


def all_possibles(xor_num):
    for i in range(256):
        if chr(i) in strictPrintables:
            if chr(i ^ xor_num) in strictPrintables:
                print(chr(i), chr(i ^ xor_num))
all_possibles(80)


print(xored_chars[76])

for i in range(55, len(xored_chars) - 12):
    available_text = "e of plaintext used in codebreaking"
    #available_text = "flag is easyctf{otp_bu7_cr1b_dr4gz"
    other_chars = []
    for j in range(len(available_text)):
        other_chars.append(chr(xored_chars[i+j] ^ ord(available_text[j])))
    
    can_print = True
    for c in other_chars:
        if not c in printables:
            can_print = False
    #print(other_chars)
    if can_print:
        print(other_chars)
        print(i)