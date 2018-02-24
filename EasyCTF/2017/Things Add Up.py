integer = int(input("Integer:"))
integers = input("Integers:")
group = []
i = ''
for char in integers:
    if not char == ' ':
        i += char
    else:
        group.append(int(i))
        i = ''
group.append(int(i))
total = 0
for a in group:
    total += a
print(total)
