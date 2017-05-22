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


def ExtendedEuclidean(a,b):
    r0 = a;
    r1 = b;
    x0 = 1;
    x1 = 0;
    y0 = 0;
    y1 = 1;
    z = [r0,x0,y0];
    while r1>0:
        r = r0%r1;
        q = (r0-r)/r1;
        x = x0-q*x1;
        y = y0-q*y1;
        z = [r1,x1,y1];
        x0 = x1;
        y0 = y1;
        x1 = x;
        y1 = y;
        r0 = r1;
        r1 = r;
    print("\ngcd(", a, ",", b, ") =", r0, "\nWeight s: ", x0, "\nWeight t: ", y0);

a = 65537;
b = 65539;
ExtendedEuclidean(a,b);
s1 = 32769
s2 = -32768
print(a * s1 + b * s2)

c1 = 144854318512202093995712983927352819432969011506679050938870376048010266887438255800654405116284539796113708005350752006554902506664890945268858621572096617935412016648508771826178522160816326675183728822464208131730918535371070163487882627176658183070499465387080308798520783628284938135878552054270553205081

c2 = 43777463096401648349314478660700518076649976722419560562817630268683953913074204594853119657353762335201100579127186171706325295455074925699159596859600819367126174739156373390407462691661386507311456139873705098033742208140365737162832055695782135447105275930060809193612438811138447009775904521421041063703

e1 = 65537

e2 = 65539

n = 148690723547194493171931181687499395275203908184366593004678640096856701816003881953771164721265186594260734477189518222023594802416422415211946513531814221018778572158314762947155346028909674646033881326232438196025177077668983620118452989999322999933833123122872424747503313470929182153562529274254334410709
em2 = modinv(c2, n)
m = pow(c1, s1, n) * pow(em2, -s2, n) % n
answer = hex(m)[2:]
answer = answer[0:len(answer) - 1]
print(unhexlify(answer))
