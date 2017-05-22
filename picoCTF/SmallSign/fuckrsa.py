val = 0
list = [2, 3, 5]
for i in range(7, 1000):
    for j in range(2, i // 2):
        if (i % j == 0):
            val = 1
            break
    if (val == 0):
        list.append(i)
    else:
        val = 0
print(list)

file = open("inputs", "w")
for i in list:
    file.write(str(i) + "\n")
file.write("-1" + "\n")
