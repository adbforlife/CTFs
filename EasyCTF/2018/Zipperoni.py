from base64 import *
from binascii import *
import math
import sha
from zipfile import *


printables = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
weirdCharacters = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
strictPrintables = "0123456789abcdefghijklmnopqrstuvwxyz_}{ "

capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numerals = "0123456789"

pattern = "a0aa__"
target = "e8ba861c8bc62328f07c7fbbf62766f9969b58dc"
password = "w8bs__"
filename = "zip_files/d71d7308dc2c.zip"


def unzip(source_filename, dest_dir, password):
    with ZipFile(source_filename) as zf:
        zf.extractall(dest_dir, pwd = password)





def test():
    sequence = []
    for i in pattern:
        if i == 'A':
            sequence.append(capitals)
        elif i == 'a':
            sequence.append(lower_case)
        elif i == '0':
            sequence.append(numerals)
        elif i == '_':
            sequence.append("_")
        else:
            print("WTF")

    for a in sequence[0]:
        for b in sequence[1]:
            for c in sequence[2]:
                for d in sequence[3]:
                    for e in sequence[4]:
                        for f in sequence[5]:
                            if sha.new(str(a) + str(b) + str(c) + str(d) + str(e) + str(f)).hexdigest() == target:
                                print(str(a) + str(b) + str(c) + str(d) + str(e) + str(f))
                                return str(a) + str(b) + str(c) + str(d) + str(e) + str(f)


while True:
    unzip(filename, "zip_files", password)
    with open("zip_files/filename.txt") as file:
        filename = file.read().rstrip()
    with open("zip_files/hash.txt") as file:
        target = file.read().rstrip()
    with open("zip_files/pattern.txt") as file:
        pattern = file.read().rstrip()
    password = test()





