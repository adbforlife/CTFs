import RSAwienerHacker
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

#def bits_to_string(b):
#    return ''.join([bits_to_char(b[i:i + ASCII_BITS])
#        for i in range(0, len(b), ASCII_BITS)])

p = 33596431795794802259658411326223835049670038095439075643702046111721496123512789
q = 33245539414916716227474847674265246888396270834737447462914355137071185675767497
e = 376647758248581566138300017722879849956696871785862459825490313268983994129862557840175774585232117260964144711496434813786561467755958254309659460042147859956187337104601365167666901157233859066817633888697347077205776581721016650863287585591220212788260238420299192452451909167928359660512078363200295448647
c = "AY6EBKk4/q8EdPFuhWcBxceqmQ8sWkyYqtvcFe/hggEKKELHnmzHZDLhjAtdir16WhpqLZibqlFJYTQcFu/Q0ndV5Nu2rMiVruiUOSizmALtwxp7w7R+qGk/1CktLMZcqltPyZwUg4Hliv9/qvNpKT2O1r4Qnk1Sp+x9OobG8e8u"
n = 747029114205618891127798494894529628078097847258053932189274215170023733206800787451955360976284714308406385279891020353829581942230430785690548403798187494292383103521408046976414140819387017767795861508304541156006698886438103962512966807396864050647825600358912639747614520824952374327376400318639894390411
lambdaN = lcm(p - 1, q - 1)
d = RSAwienerHacker.hack_RSA(e,n)
c = int(hexlify(b64decode(c)), 16)
m = pow(c, d, n)
print(bin(m))
