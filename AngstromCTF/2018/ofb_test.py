#(ax1 + c) mod m = b1
#(ax2 + c) mod m = b2
#(ax3 + c) mod m = b3
#(a(x1-x2)) mod m = b1 - b2
#ax mod m = b

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

m = pow(2, 32)
x1 = 2445943554
x2 = 2225636917
x3 = 1320590709
b1 = 2225636917
b2 = 1320590709
b3 = 4196912501
x = 220306637
b = 905046208
A = -1128812539
base = b * A
a = 3204287424
c = 1460809397
print((a * x2 + c) % m)