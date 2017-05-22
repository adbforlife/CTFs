import math

def gcd(a, b):
    m = max(a, b)
    n = min(a, b)
    while not m % n == 0:
        big = max(n, m - n)
        small = min(n, m - n)
        m = big
        n = small
    return n

def lcm(a, b):
    return a * b // gcd(a, b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

#def bits_to_string(b):
#    return ''.join([bits_to_char(b[i:i + ASCII_BITS])
#        for i in range(0, len(b), ASCII_BITS)])

p = 61
q = 53
e = 17
c = 2790
n = p * q
lambdaN = lcm(p - 1, q - 1)
d = modinv(e, lambdaN)
m = pow(c, d, n)
print(m)

p = 723729521656711874869
q = 438909609138481458361
e = 65537
c = 103708797371272023634570175779915363680246
n = p * q
lambdaN = lcm(p - 1, q - 1)
d = modinv(e, lambdaN)
m = pow(c, d, n)
print(m)
print(len(str(m)))
#print(bits_to_string(m))
for i in range(len(str(m))):
    if i % 3 == 2:
        text = ""
        text += str(m)[i-2]
        text += str(m)[i-1]
        text += str(m)[i]
print(len(bin(m)))
print(bin(m))
