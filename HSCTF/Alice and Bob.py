import math
def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s
modulus = 8911991767204557841
pubA = 1317032838957486192
base = 987
a = 1201905
pubB = 731665363559374475
b = 1213832
print(pow(pubA, b, modulus))
print(pow(pubB, a, modulus))
