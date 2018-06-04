def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)

hashed = 293366475
modulo = 4294967295

printables = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
def isPrintable(string):
    for char in string:
        if not char in printables:
            return False
    return True

from itertools import combinations_with_replacement
alphabet = "abcdefghijklmnopqrstuvwxyz_,./;'[]\\"


print(hash_it("helloworld"))

for i in range(1,10):
	print(i)
	comb = combinations_with_replacement(alphabet, i)
	for j in comb:
		s = ''.join(j)
		if (hash_it(s) == hashed):
			print(s)



#print(hash_it("helloworld"))



def factor(num):
    n = num
    i = 2
    primeFactors = []
    counts = []
    result = []
    while i < 128:
        if n % i == 0:
            primeFactors.append(i)
            counts.append(1)
            n = n // i
            while n % i == 0:
                counts[len(counts) - 1] += 1
                n = n // i
        i += 1
    if n > 1:
        primeFactors.append(n)
        counts.append(1)
    for i in range(len(primeFactors)):
        for j in range(counts[i]):
            result.append(primeFactors[i])
    return result

#with open("/Users/ADB/Desktop/CTFandTools/Tools/Dictionaries/Passwords/rockyou.txt","r") as f:
#	strings = f.read().split("\n")
#	for s in strings:
#		if (isPrintable(s)):
#			if hash_it(s) == hashed:
#				print(s)
hashed += 108 * modulo
for i in range(100000):
	hashed += 127 * modulo

	result = factor(hashed)
	if result[-1] < 10000:
		#print(result)
		pass