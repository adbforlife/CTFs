primes = [2]
def isPrime(num):
    for i in primes:
        if num % i == 0:
            return False
        elif pow(i, 2) > num:
            return True
    return True
for i in range(3, 3690):
    if isPrime(i):
        primes.append(i)

list = [0 for i in range(3710)]
for i in range(10):
    list[i] = 1
for i in range(2, 411):
    for j in reversed(range(i*9+1)):
        result = 0
        for k in range(10):
            result += list[j-k]
        list[j] = result

list2 = [0 for i in range(3700)]
for i in range(10):
    list2[i] = 1
for i in range(2, 26):
    for j in reversed(range(i*9+1)):
        result = 0
        for k in range(10):
            result += list2[j-k]
        list2[j] = result

answer1 = 0
answer2 = 0
for i in primes:
    answer1 += list[i]
    answer2 += list2[i]
print((answer1 - answer2) % 1000000009)
