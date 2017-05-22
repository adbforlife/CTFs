import RSAwienerHacker
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

p = 33596431795794802259658411326223835049670038095439075643702046111721496123512789
q = 33245539414916716227474847674265246888396270834737447462914355137071185675767497
e = 3
c = 261345950255088824199206969589297492768083568554363001807292202086148198406422015406837306712350185001004539557263392747990052517553733793783164539246862722846027251864430884218012651143187891041767278036834613455255679627575565220404720823343734717216496823882624775291829042065791328110144692179931720656184
n = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
lambdaN = lcm(p - 1, q - 1)
d = RSAwienerHacker.hack_RSA(e,n)
print(d)
#m = pow(c, d, n)
#print(bin(m))