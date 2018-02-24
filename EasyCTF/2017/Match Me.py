maleFile = open("/Users/ADB/Desktop/male.txt", "r")
femaleFile = open("/Users/ADB/Desktop/female.txt", "r")
fList = femaleFile.readlines()
mList = maleFile.readlines()
mNList = [x for x in range(1000)]
fNList = [x for x in range(1000)]
mPList = [x for x in range(1000)]
fPList = [x for x in range(1000)]
for i in range(len(mList)):
    item = mList[i]
    index = item.index(" ")
    mNList[i] = item[0:index]
    wholeString = item[index + 1:]
    tempString = ""
    list = []
    for char in wholeString:
        if char == ",":
            list.append(int(tempString))
            tempString = ""
        elif char == " ":
            pass
        else:
            tempString += char
    list.append(int(tempString))
    mPList[i] = list
for i in range(len(fList)):
    item = fList[i]
    index = item.index(" ")
    fNList[i] = item[0:index]
    wholeString = item[index + 1:]
    tempString = ""
    list = []
    for char in wholeString:
        if char == ",":
            list.append(int(tempString))
            tempString = ""
        elif char == " ":
            pass
        else:
            tempString += char
    list.append(int(tempString))
    fPList[i] = list
maleFile.close()
femaleFile.close()


#mNList = ["Albert", "Bob", "Cathcart"]
#fNList = ["Alice", "Bernice", "Catherine"]
#mPList = [[3, 1, 2], [2, 1, 3], [2, 3, 1]]
#fPList = [[1, 2, 3], [3, 2, 1], [1, 2, 3]]
couples = [0 for x in range(1000)]
singleMales = [1 for x in range(1000)]
singleFemales = [1 for x in range(1000)]
while 1 in singleMales:
    for i in range(len(singleMales)):
        if singleMales[i] == 1:
            for j in range(len(mPList[i])):
                femaleIndex = mPList[i][j] - 1
                if singleFemales[femaleIndex] == 1:
                    couples[femaleIndex] = i + 1
                    singleMales[i] = 0
                    singleFemales[femaleIndex] = 0
                    break
                else:
                    preference = fPList[femaleIndex]
                    marriedMaleIndex = couples[femaleIndex] - 1
                    if preference.index(marriedMaleIndex + 1) > preference.index(i + 1):
                        couples[femaleIndex] = i + 1
                        singleMales[i] = 0
                        singleMales[marriedMaleIndex] = 1
                        break
                    else:
                        pass

couples2 = [0 for x in range(1000)]
singleMales = [1 for x in range(1000)]
singleFemales = [1 for x in range(1000)]
while 1 in singleFemales:
    for i in range(len(singleFemales)):
        if singleFemales[i] == 1:
            for j in range(len(fPList[i])):
                maleIndex = fPList[i][j] - 1
                if singleMales[maleIndex] == 1:
                    couples2[maleIndex] = i + 1
                    singleFemales[i] = 0
                    singleMales[maleIndex] = 0
                    break
                else:
                    preference = mPList[maleIndex]
                    marriedFemaleIndex = couples2[maleIndex] - 1
                    if preference.index(marriedFemaleIndex + 1) > preference.index(i + 1):
                        couples2[maleIndex] = i + 1
                        singleFemales[i] = 0
                        singleFemales[marriedFemaleIndex] = 1
                        break
                    else:
                        pass

stableCouples = []
for i in range(len(couples2)):
    if couples[couples2[i] - 1] == i + 1:
        stableCouples.append([mNList[i], fNList[couples2[i] - 1]])
result = ""
for i in range(len(stableCouples)):
    result += "("
    result += stableCouples[i][0]
    result += ","
    result += stableCouples[i][1]
    result += ")"
print(result)
