list = [142, 162, 145, 156, 144, 141, 137, 142, 145, 145, 162, 171]
string = ""
for i in list:
    string += chr(int(str(i), 8))
print(string)
