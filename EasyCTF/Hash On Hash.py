file = open("/Users/ADB/Desktop/0c4dc9d2255aebe12ffdb0b74b5b470708d54daf_hexstrings copy.txt", "r")
hexString = file.readlines()
hexString = [x.strip() for x in hexString]
print(len(hexString))
diffString = []
frequencyList = []
for string in hexString:
    if string in diffString:
        frequencyList[diffString.index(string)] += 1
    else:
        diffString.append(string)
        frequencyList.append(1)
for i in range(len(diffString)):
    print(frequencyList[i], diffString[i])
print(len(frequencyList))
file.close()
