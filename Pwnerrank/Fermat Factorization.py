import math
from binascii import *
from fractions import *
import gmpy2

def fermat_factor(n):
    assert n % 2 != 0
    
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    
    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)

return int(p), int(q)

print(fermat_factor(55089599753625499150129246679078411260946554356961748980861372828434789664694269460953507615455541204658984798121874916511031276020889949113155608279765385693784204971246654484161179832345357692487854383961212865469152326807704510472371156179457167612793412416133943976901478047318514990960333355366785001217))

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

p = 7422236843002619998657542152935407597465626963556444983366482781089760760914403641211700959458736191688739694068306773186013683526913015038631710959988771
q = 7422236843002619998657542152935407597465626963556444983366482781089760759017266051147512413638949173306397011800331344424158682304439958652982994939276427
e = 65537
c = 37955771050328151356097380633042584587316105205149857375584557832574323922346169799330369178454500710400244535879484118031474111876767744790681441191680904735656729191836699720068958970475398893921485939252213096132678570289120947595520728495469071141082805478126488147184313388673848879996747649690130803256
n = p * q
print(n == 55089599753625499150129246679078411260946554356961748980861372828434789664694269460953507615455541204658984798121874916511031276020889949113155608279765385693784204971246654484161179832345357692487854383961212865469152326807704510472371156179457167612793412416133943976901478047318514990960333355366785001217)
lambdaN = lcm(p - 1, q - 1)
print("hey")
d = modinv(e, lambdaN)
m = pow(c, d, n)
print("hey")
print(unhexlify(hex(m)[2:-1]))


