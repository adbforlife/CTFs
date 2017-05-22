from functools import *
import operator
import math

print(12/4)

jkx = 425
# REDACTED
pork = jkx - 1
jkx *= pork
pp = list(filter(lambda g: not any(g % u == 0 for u in range(2, g)), range(2, 300)))
print(pp)
print(jkx)
b = reduce(operator.mul, (pp[i] ** int(str(jkx)[i]) for i in range(len(str(jkx)))))
s = 2184719430548746797018052999592211492090202845543009868618737194688235684230309853968772897679203241383062752895842272234666418301968390697389887530219762749385171623700534235833400047104536066118418848666095683701880968896640969197604426909584865157420723150000
print(s / b)
print(len(str(s)))



def findFactors(num):
    n = num
    i = 2
    primeFactors = []
    counts = []
    factors = []
    while n >= i ** 2:
        #print(n)
        if n % i == 0:
            primeFactors.append(i)
            counts.append(1)
            n = n // i
            while n % i == 0:
                counts[len(counts) - 1] += 1
                n = n // i
        elif i in pp:
            primeFactors.append(i)
            counts.append(0)
        i += 1
    if n > 1:
        primeFactors.append(n)
        counts.append(1)
    print(primeFactors, counts)
    string = ""
    for i in counts:
        string += str(i)
    print(string)
    return factors
findFactors(22801)
findFactors(s)

print((1+int(math.sqrt(1+4 * 425105275369825839469807200515239812)))//2)
print(652000978043611404 * 652000978043611403)
