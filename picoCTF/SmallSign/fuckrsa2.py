primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
file = open("results", "r")
list = file.readlines()
n = int(list[1][3:len(list[1])-1])
numList = []
for i in list:
    if (i[0] == "E"):
        numList.append(i)
for i in range(len(numList)):
    numList[i] = numList[i][48:len(numList[i]) - 1]
numList.pop()
challenge = numList[len(numList) - 1]
numList.pop()
print(numList[len(numList) - 1])
print(challenge)
def factor(num):
    n = num
    i = 2
    primeFactors = []
    counts = []
    result = []
    while n >= i ** 2:
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
factors = factor(int(challenge))
print(factors)
final = 1
print(factors[len(factors) - 1])
if factors[len(factors) - 1] < 1000:
    for i in range(len(factors)):
        final = final * int(numList[primes.index(factors[i])]) % n
print(final)
