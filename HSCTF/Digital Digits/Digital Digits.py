with open("/Users/ADB/Desktop/digital_0636b59ded5db7826112b3826694054e071c56d9ce7536a1bb149765dd6c5e28.txt", "r") as file:
    string = file.read().rstrip()
    #string = "12345"
    possibles = [0 for i in range(9)]
    for i in string:
        num = int(i)
        newPossibles = [0 for x in range(9)]
        for j in range(len(newPossibles)):
            newPossibles[j] = possibles[j] + possibles[(j-num)%9]
        newPossibles[num%9] += 1
        for j in range(9):
            possibles[j] = newPossibles[j]
    for i in range(len(possibles)):
        possibles[i] = possibles[i] % 1000000003
    print(possibles)
