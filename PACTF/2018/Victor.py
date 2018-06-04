c = "7264160199640987865519282923616105"
key = "1226199112261991122619911226199112"
string = ""
for i in range(len(c)):
	string += str((int(c[i]) - int(key[i])) % 10)
print(string)
message = "6 04 8 07 1 08 74 8 90 96 74 3 90 03 71 70 75 2 70 93"