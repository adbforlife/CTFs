file = open("/Users/ADB/Desktop/strings.dat", "r")
strings = file.readlines()
count = 0
for string in strings:
    countChar = 0
    for char in string:
        if char == "E" or char == "e":
            countChar += 1
    if countChar > 4 and countChar % 2 == 1:
        count += 1
print(count)
