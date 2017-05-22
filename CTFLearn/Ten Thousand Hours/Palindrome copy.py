file = open("/Users/ADB/Desktop/Bad/desired", "r")
strings = file.readlines()
file.close()
file2 = open("/Users/ADB/Desktop/Bad/super_encrypted", "r")
encrypted = file2.readlines()
count = 0
for i in encrypted:
    for j in range(len(strings)):
        if i.rstrip() == strings[j].rstrip():
            count += 1
print(count)
