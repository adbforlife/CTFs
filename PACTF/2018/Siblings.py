from Crypto.PublicKey import RSA
from gmpy2 import *
from binascii import *
public_keys = []
for i in range(20):
	public_key = RSA.importKey(open('/Users/ADB/Desktop/static/public_keys/key' + str(i) + '.pem', 'r').read())
	public_keys.append(public_key)
e = 65537
n = []
for key in public_keys:
	n.append(key.n)
private_keys = []
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] != n[j] and gcd(n[i],n[j]) != 1:
            print(i,j)
            p = gcd(n[i],n[j])
            q = n[i] // p
            private_keys.append([p,q,e])

print(len(private_keys))

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

def get_message(c, p, q, e):
    n = p * q
    lambdaN = lcm(p - 1, q - 1)
    d = modinv(e, lambdaN)
    m = powmod(c, d, n)
    return m

with open("/Users/ADB/Desktop/static/unbreakable_code", "r") as f:
    c = f.read()
c = int(hexlify(c),16)
for i in range(len(private_keys))[::-1]:
    c = get_message(c,private_keys[i][0],private_keys[i][1],private_keys[i][2])
result = format(c, 'x')
if len(result) % 2 == 1:
    result = '0' + result
print(unhexlify(result))





