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

p = 277271726050281009396301232126405463677
q = 224258454597761606450883324956139951511
e = 65537
d = 10810931767876665036391364653054260523419878402727343505431379711767076903333
dp = d % (p - 1)
dq = d % (q - 1)
qinv =  modinv(q, p)
n = p * q

print("n", n)
print("p", p)
print("q", q)
print("e", e)
print("d", d)
print("dp", dp)
print("dq", dq)
print("qinv", qinv)

print("n", hex(n))
print("p", hex(p))
print("q", hex(q))
print("e", hex(e))
print("d", hex(d))
print("dp", hex(dp))
print("dq", hex(dq))
print("qinv", hex(qinv))

n = p * q
lambdaN = lcm(p - 1, q - 1)
d = modinv(e, lambdaN)
