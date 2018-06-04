from hashlib import *
desired = "1b657b7fe26eda5b3c1309d340f1674d"
strings = ["a", "b", "c"]
available = "abc"
for i in range(14):
    print(i)
    strings2 = []
    strings3 = []
    for j in strings:
        strings2.append(j)
        strings3.append(j)
    for j in range(len(strings)):
        strings[j] = strings[j] + "a"
    for j in range(len(strings2)):
        strings2[j] = strings2[j] + "b"
    for j in range(len(strings3)):
        strings3[j] = strings3[j] + "c"
    strings = strings + strings2 + strings3

#file = open("/Users/ADB/Desktop/test", "w")
#for i in strings:
#    file.write(i + "\n")
#file.close()
previous = "d"
for i in strings:
    if not i[12] == previous:
        print(i)
        previous = i[12]
    if md5(i).hexdigest() == desired:
        print("success", i)
        break
