file = open("/Users/ADB/Desktop/data.txt", "r")
strings = file.readlines()
file.close()
suits = ["Clubs", "Diamonds", "Hearts", "Spades", "Joker"]
yourInitialCards = []
opponentInitialCards = []
yourCards = ["?" for i in range(27)]
opponentCards = ["?" for i in range(27)]
def numOfSuits(string):
    count = 0
    for i in suits:
        count += string.count(i)
    return count
for i in range(len(strings)):
    string = strings[i]
    if numOfSuits(string) == 1 and not "opponent" in string:
        opponentString = strings[i-1]
        yourCard = string[string.index(":") + 2 : -1]
        opponentCard = opponentString[opponentString.index(":") + 2 : -1]
        if len(yourInitialCards) < 27:
            yourInitialCards.append(yourCard)
        if len(opponentInitialCards) < 27:
            opponentInitialCards.append(opponentCard)
        if "War" in strings[i+1]:
            cardStringOpponent = strings[i+2][strings[i+2].index(")") + 2 : -1]
            cardStringYou = strings[i+3][strings[i+3].index(")") + 2 : -1]
            opponentString1 = cardStringOpponent[0:cardStringOpponent.index("and") - 1]
            opponentString2 = cardStringOpponent[cardStringOpponent.index(")") + 2:]
            youString1 = cardStringYou[0:cardStringYou.index("and") - 1]
            #youString2 is messed up
            youString2 = cardStringYou[cardStringYou.index(")") + 2:]
            if len(yourInitialCards) < 27:
                yourInitialCards.append(youString1)
                yourInitialCards.append(yourCards[2])
            if len(opponentInitialCards) < 27:
                opponentInitialCards.append(opponentString1)
                opponentInitialCards.append(opponentString2)
            if "opponent" in strings[i+4]:
                #winner is opponent
                del opponentCards[0]
                del opponentCards[0]
                del opponentCards[0]
                del yourCards[0]
                del yourCards[0]
                messedUpCard = yourCards[0]
                del yourCards[0]
                opponentCards.append(opponentCard)
                opponentCards.append(yourCard)
                opponentCards.append(opponentString1)
                opponentCards.append(youString1)
                opponentCards.append(opponentString2)
                opponentCards.append(messedUpCard)
            else:
                #winner is you
                del opponentCards[0]
                del opponentCards[0]
                del opponentCards[0]
                del yourCards[0]
                del yourCards[0]
                messedUpCard = yourCards[0]
                del yourCards[0]
                yourCards.append(opponentCard)
                yourCards.append(yourCard)
                yourCards.append(opponentString1)
                yourCards.append(youString1)
                yourCards.append(opponentString2)
                yourCards.append(messedUpCard)
        elif "opponent" in strings[i+1]:
            #winner is opponent
            del yourCards[0]
            del opponentCards[0]
            opponentCards.append(opponentCard)
            opponentCards.append(yourCard)
        else:
            #winner is you
            del yourCards[0]
            del opponentCards[0]
            yourCards.append(opponentCard)
            yourCards.append(yourCard)

def printCards(cards):
    keyString = ""
    for i in cards:
        if i == "Joker A":
            keyString += "A "
        elif i == "Joker B":
            keyString += "B "
        else:
            if i[0:2] == "10":
                keyString += "T"
            else:
                keyString += i[0]
            keyString += i[i.index("of") + 3].lower()
            keyString += " "
    print(keyString)

yourInitialCards[yourInitialCards.index("Joker A") + 1] = "Queen of Clubs"
yourInitialCards[yourInitialCards.index("5 of Spades") + 1] = "9 of Clubs"
yourInitialCards[yourInitialCards.index("8 of Clubs") + 1] = "10 of Hearts"

printCards(yourInitialCards + opponentInitialCards)
printCards(opponentInitialCards + yourInitialCards)
printCards((yourInitialCards + opponentInitialCards)[::-1])
printCards((opponentInitialCards + yourInitialCards)[::-1])
printCards(opponentCards)
printCards(opponentCards[::-1])
