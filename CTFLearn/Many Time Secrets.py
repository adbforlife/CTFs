from base64 import *
from binascii import *
import math
from scipy import stats

printables = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
weirdCharacters = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
strictPrintables = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ \"'"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
nullHypothesis = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.024, 0.002, 0.02, 0.001]

def countFrequencies(string):
    frequencyCounts = [0 for i in range(26)]
    for char in string:
        if char in alphabet:
            charIndex = alphabet.index(char) % 26
            frequencyCounts[charIndex] += 1
    return frequencyCounts

def chi2pValue(string):
    frequencies = countFrequencies(string)
    expectedCounts = [0 for i in range(26)]
    statistic = 0.0
    sampleSize = 0
    for i in frequencies:
        sampleSize += i
    for i in range(len(nullHypothesis)):
        expectedCounts[i] = round(nullHypothesis[i] * sampleSize, 3)
    for i in range(len(frequencies)):
        if not expectedCounts[i] == 0:
            statistic += (frequencies[i] - expectedCounts[i]) ** 2 / expectedCounts[i]
        else:
            statistic += (frequencies[i] - expectedCounts[i]) ** 2 / 1
    return 1 - stats.chi2.cdf(statistic, sampleSize - 1)

def isPrintable(string):
    for char in string:
        if not char in printables:
            return False
    return True

def isWeird(string):
    count = 0
    for char in string:
        if char in weirdCharacters:
            count += 1
    if count > len(string) // 1000:
        return True
    return False

def repeatXOR(string, key):
    longkey = key * (len(string) // len(key)) + key[0:len(string) % len(key)]
    hexresult = hex(int(hexlify(longkey), 16) ^ int(hexlify(string), 16))[2:]
    if hexresult[len(hexresult) - 1] == "L":
        hexresult = hexresult[0:len(hexresult) - 1]
    if len(hexresult) % 2 == 1:
        hexresult = "0" + hexresult
    return hexresult

line1 = "0529242a631234122d2b36697f13272c207f2021283a6b0c7908"
line2 = "2f28202a302029142c653f3c7f2a2636273e3f2d653e25217908"
line3 = "322921780c3a235b3c2c3f207f372e21733a3a2b37263b313012"
line4 = "2f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d"
line5 = "283f652c2b31661426292b653a292c372a2f20212a316b283c09"
line6 = "29232178373c270f682c216532263b2d3632353c2c3c2a293504"
line7 = "613c37373531285b3c2a72273a67212a277f373a243c20203d5d"
line8 = "243a202a633d205b3c2d3765342236653a2c7423202f3f652a18"
line9 = "2239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c"
line10 = "263e203d63232f0f20653f207f332065262c3168313722367918"
line11 = "2f2f372133202f142665212637222220733e383f2426386b"

def brute(string, line):
    return unhexlify(repeatXOR(string, unhexlify(line)))

flagString = "ALEXCTF{HERE_GOES_THE_KEY}"
print("1", brute(flagString, line1))
print("2", brute(flagString, line2))
print("3", brute(flagString, line3))
print(brute("sed One time pad encryption", line3))
print("4", brute(flagString, line4))
print("5", brute(flagString, line5))
print(brute("is the only encryption", line5))
print("6", brute(flagString, line6))
print("7", brute(flagString, line7))
print(brute(" proven to be not crack", line7))
print("8", brute(flagString, line8))
print(brute("ever if the key is kept secret", line8))
print("9", brute(flagString, line9))
print("10", brute(flagString, line10))
print("11", brute("ALEXCTF{HERE_GOES", line11))
