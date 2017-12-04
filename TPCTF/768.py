n = 0xCAD984557C97E039431A226AD727F0C6D43EF3D418469F1B375049B229843EE9F83B1F97738AC274F5F61F401F21F1913E4B64BB31B55A38D398C0DFED00B1392F0889711C44B359E7976C617FCC734F06E3E95C26476091B52F462E79413DB5
e = 0x10001
c = 0x3F808414886E7C91F1D78AEB7EF920D2C9294AC384DCBB1A48032E8CAB79131AB3C1852896EEEECB5BA055AE77BBB619741FDE4D01AAC7D56F4E44508A8FC81A86DDB929A112AA80C4A7221B3C651E14E2D701B52E295152813CD9EFB4B51CB
p = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
q = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917
print (n == p * q)

import math
from fractions import *
from binascii import *

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

def rsaD(c, d, n):
    m = pow(c, d, n)
    result = format(m, 'x')
    if len(result) % 2 == 1:
        result = '0' + result
    return unhexlify(result)

def rsaPQ(c, p, q, e):
    n = p * q
    lambdaN = lcm(p - 1, q - 1)
    d = modinv(e, lambdaN)
    m = pow(c, d, n)
    result = format(m, 'x')
    if len(result) % 2 == 1:
        result = '0' + result
    return unhexlify(result)
   
print(rsaPQ(c, p, q, e))