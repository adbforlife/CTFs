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

def singleByteXORCipher(string):
    answer = []
    temp = ""
    trials = []
    for i in range(0, 256):
        hexresult = hex(i)[2:]
        if len(hexresult) % 2 == 1:
            hexresult = "0" + hexresult
        trials.append(unhexlify(hexresult))
    for char in trials:
        temp = unhexlify(repeatXOR(string, char))
        print(temp)
        if isPrintable(temp):
            if chi2pValue(temp) > 0.001:
                answer.append(temp)
    return answer


with open("flag.png.crypt", "r") as f:
	string = f.read().rstrip()
	#string.replace(" ", "")
	#string.replace("\n", "")
	#print(string)

new_string = repeatXOR(string, unhexlify("ee"))
print(new_string)

with open("black-2189644_960_720.png", "w") as f:
	f.write(unhexlify(new_string))


