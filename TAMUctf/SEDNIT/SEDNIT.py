import math
from base64 import *
from binascii import *

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

file = open("/Users/ADB/Desktop/text", "r")
strings = file.readlines()
reality = []
for i in strings:
    string = ""
    for char in i:
        if not char == "\x00":
            string += char
    reality.append(string)
for i in reality:
    print(i)

c = "Hpocva/tLxIigotSzrQKU9CVHPTfSO8YyxHCmznDYwuCCMwAzo44vO7JlVRpaCp2uzvTdH7lO4SxCOuPUuPFDVIbgcfA3vIWYR5n5Ko+mXpW2pqSB/RFJr/qzCGl54n63X343wMgMqz9jrN+p2N1Qf4ALv8WhfK/oIrkwGiaMkQ="

n = "d43cb226240bc3ee1f1081c8318f4aed53f3d1dd5d51301af780c34499b47282dccbf1752134d298d8e00ebfa310e5228d933f9fc87dceb70f9f003829a3579a6ce1b5bb244be8fee445e17514dfff6a8649132f30d9c1feed80ed56dc720a278d766abd7af3eeccc3f0981eb36af72491444b127b6ec16165ee5abdd2b5b7c3"
e = "10001"
d = "8a42f8338cabf579fcd6be1572e3cc860b78fd30de87f374bde42e5154688f68dcfa27548ccb629e9c3a6aa14153d251ce352cefa4a700b195059a18fc5722cb918a6f502bdb1229923520432a342915ef802d73b5b7c78a198e433bf05d2900bda100df4d84138969b06601e0d9c993fc42785685896a6410e25b0ce90b85e1"
n = int(n, 16)
d = int(d, 16)
c = int(hexlify(b64decode(c)), 16)
m = pow(c, d, n)
answer = hex(m)
hex(
