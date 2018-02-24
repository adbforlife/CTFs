from base64 import *
from binascii import *
import math
from scipy import stats

c = "000c1c1516190315121f03020a030f000f02061403010e0b1e0f0d0315020e080516141f1b191d0713050918180e010c0d0001011c1e05151909111609151714130b100b1519011c1f0613"

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


wordlist = []
with open("/Users/ADB/Desktop/words.txt", "r") as file:
    for string in file.readlines():
        wordlist.append(string.rstrip())

target = "emolumen"
alphabet = "abcdefghijklmnopqrstuvwxyz"
def vigenere(word1, word2):
    string1 = (word1 * 8)[:8]
    string2 = (word2 * 8)[:8]
    result = ""
    for i in range(8):
        result += alphabet[(alphabet.index(string1[i]) + alphabet.index(string2[i])) % 26]
    return result

print(unhexlify(repeatXOR(unhexlify(c), "easyctf{flag")))
possible_words = []
for i in wordlist:
    if i[:2] == "be":
        possible_words.append(i)

for i in possible_words:
    possible_answer = unhexlify(repeatXOR(unhexlify(c), "emoluments" + i))
    if not "`" in possible_answer:
        print(possible_answer)

word1 = "emoluments"
#for i in range(20):
#    print(unhexlify(repeatXOR(unhexlify(c), word1 + unhexlify("ff") * i)))

#for i in range(len(wordlist) - 1):
#    if i % 100 == 0:
#        print(i)
#    for j in range(i, len(wordlist)):
#        if vigenere(wordlist[i], wordlist[j]) == target:
#            print(wordlist[i], wordlist[j])
#            print("f yeah")

#for i in range(len(wordlist)):
#    if i % 100 == 0:
#        print(i)
#    for j in range(len(wordlist)):
#        possible = unhexlify(repeatXOR(test, wordlist[i] + wordlist[j]))
#        if isPrintable(possible) and "easyctf" in possible:
#            print(possible)

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

def singleByteXORCipherOneSolution(string):
    answer = ""
    temp = ""
    trials = []
    for i in range(0, 256):
        hexresult = hex(i)[2:]
        if len(hexresult) % 2 == 1:
            hexresult = "0" + hexresult
        trials.append(unhexlify(hexresult))
    maximumPValue = 0.0
    for char in trials:
        temp = unhexlify(repeatXOR(string, char))
        if isPrintable(temp):
            if not isWeird(temp):
                if chi2pValue(temp) > maximumPValue:
                    answer = temp
                    maximumPValue = chi2pValue(temp)
    return answer

def hammingDistance(string1, string2):
    distance = bin(int(hexlify(string1), 16) ^ int(hexlify(string2), 16))
    result = 0
    for char in distance:
        if char == "1":
            result += 1
    return result

def findKeySizes(string, minimum = 2, maximum = 40):
    hammingDistances = []
    keySizes = []
    for i in range(minimum, maximum + 1):
        distance = (hammingDistance(string[0:i], string[i:2*i]) + hammingDistance(string[i:2*i], string[2*i:3*i]) + hammingDistance(string[2*i:3*i], string[3*i:4*i])) / 3.0 / i
        hammingDistances.append(distance)
    index1 = hammingDistances.index(min(hammingDistances))
    keySizes.append(index1 + minimum)
    hammingDistances[index1] = 10.0
    index2 = hammingDistances.index(min(hammingDistances))
    keySizes.append(index2 + minimum)
    hammingDistances[index2] = 10.0
    index3 = hammingDistances.index(min(hammingDistances))
    keySizes.append(index3 + minimum)
    hammingDistances[index3] = 10.0
    index4 = hammingDistances.index(min(hammingDistances))
    keySizes.append(index4 + minimum)
    hammingDistances[index4] = 10.0
    index5 = hammingDistances.index(min(hammingDistances))
    keySizes.append(index5 + minimum)
    return keySizes

def transposition(string, keySizes):
    results = []
    for i in keySizes:
        result = []
        for j in range(i):
            result.append("")
        for j in range(len(string)):
            result[j%i] += string[j]
        results.append(result)
    return results

def combination(strings):
    answer = ""
    for i in range(len(strings[0])):
        for j in range(len(strings)):
            if len(strings[j]) > i:
                answer += strings[j][i]
    return answer

def vigenereSolve(string, minimumKeySize = 2, maximumKeySize = 40):
    results = transposition(string, minimumKeySize, maximumKeySize)
    answers = []
    for i in results:
        group = []
        possibles = []
        for j in i:
            group.append(singleByteXORCipher(j))
        for j in group:
            for k in range(len(j)):
                if k == 0:
                    for n in possibles:
                        n.append(j[k])
                else:
                    possiblesTemp = possibles
                    for n in possiblesTemp:
                        n.append(j[k])
                    possibles = possibles + possiblesTemp
        for j in possibles:
            answers.append(combination(j))
    return answers

def vigenereSolveOneSolutionForEachLength(string, minimumKeySize = 2, maximumKeySize = 40):
    keySizes = findKeySizes(string, minimumKeySize, maximumKeySize)
    results = transposition(string, keySizes)
    answers = []
    for i in results:
        group = []
        for j in i:
            solution = singleByteXORCipherOneSolution(j)
            print(solution)
            group.append(solution)
        answers.append(combination(group))
    return answers

def vigenereSolveOneSolutionForEachLengthAllKeySizes(string, minimumKeySize = 2, maximumKeySize = 40):
    keySizes = []
    for i in range(2, 41):
        keySizes.append(i)
    results = transposition(string, keySizes)
    answers = []
    for i in results:
        group = []
        for j in i:
            group.append(singleByteXORCipherOneSolution(j))
        answers.append(combination(group))
    return answers


