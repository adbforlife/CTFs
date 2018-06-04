def isValid(num):
	n = []
	for i in str(num):
		n.append(int(str(i)))
	#print(n)
	for i in range(len(n)):
		if i % 2 == 0:
			n[i] = n[i] * 2
			if len(str(n[i])) > 1:
				n[i] = int(str(str(n[i])[0])) + int(str(str(n[i])[1]))
	if sum(n) % 10 == 0:
		return True
	return False

with open("/Users/ADB/Desktop/cc_leak.txt", "r") as f:
	numbers = map(int, f.read().rstrip().split("\n"))
	for i in range(len(numbers)):
		if not isValid(numbers[i]):
			print(numbers[i])
			pass