n = 65561
e = 65537
c = 27830
m = 1
while pow(m, e, n) != c:
	m += 1
print(m)