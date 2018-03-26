import math
import gmpy2
from base64 import *
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
    m = gmpy2.powmod(c, d, n)
    result = format(m, 'x')
    if len(result) % 2 == 1:
        result = '0' + result
    return unhexlify(result)

e = 0x10001
n = 36511974694593690272644354864534934200522045623187752384823594729275730789191680514905027084950729514148679507005058047146031869995768765034876499069680202424692876360895377987654388335335689563844006584610187090074654410815638237841872991488680663410743679302763304922852173164820002226109196761249018548478251723505481964749218302723593776180246783117481280725673997940309717028451914887375722437833384305529884261542397905220138488012276363046571670926597766521674838665982314321651508118240682649024780239598188845543243957916954287138820155843952556411235376764737602711594439293285811102883736229645274092478611
d = modinv(e, n - 1)
c = "Cc0GtEY4nL7DhDukClWKaTHChrCVJeVVm3MJ+6hgiqaYUjbx9ArCrH0uzdfDqf4l81NAqV0fGtd8a9H4dlEQRykvOwpFpViK4qTU1H28nEMZ6O1Hnt9NrLxlSvpARZd8hxoJtXiwUbZI6rcI9lQwt+pJLvrvw2/Mz+fBMvrVPFONSYDH/lU0wy4jKbH0zl7zJ09+gCBo9oJ2Hqpsh0BkcS6ix5lDu/6JENG/ChC7jZGYWpte+QIkb/fQTwsw3tGIz1jWYhqQ8MrSxtGpyyPG9Oy/zGHIBEBDesS4r72D8n2mQExRnCH2KW5wz5hsM2TXYRILtJqWCOyv/AF56Ebg9A=="
c = int(hexlify(b64decode(c)), 16)
print(format(pow(c, d, n), 'x'))


#c = 7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120
#p = 86682053881033548130239572295864644283804537304657306684316407835856200763097
#q = 106684212123257830963763477904396907546443625631948829795328565994342339155077
#e = 11 * 41 * 67623079903 * 5161910578063 * 175238643578591220695210061216092361657427152135258210375005373467710731238260448371371798471959129039441888531548193154205671
#print(rsaPQ(c, p, q, e))