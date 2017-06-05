string = "2-1-3-11-23-1-18-4-19-8-19-1-2-13-12-18-7-6-18-7-18-8-25-6-8-19-6-3-21-19-5-16-21-3-11-5-6-19-16-8-15-21-25-10-23-11-9-5-1-9-1-17-23-12-18"
strings = string.split("-")
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
for i in strings:
    result += alphabet[int(i)-1]
print(result)
string = "rlwqaiaeikwjyuohpsfekcupesucfshfyhrgrfgrlmbash"
newString = ""
for i in string:
    newString += alphabet[25 - alphabet.index(i)]
print(newString)
string = "iodjzrzvrpdqbflskhuvpxfkvhfxuh"
