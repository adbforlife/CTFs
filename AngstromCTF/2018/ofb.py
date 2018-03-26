import struct

def lcg(m, a, c, x):
	return (a*x + c) % m

m = pow(2, 32)

with open('flag.png.enc', "r") as f:
	string = f.read()
	print(len(string))

with open('flag.png', "w") as f:
	new_string = "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52"
	while len(new_string) < 58788 - 8:
		new_string += "\x00"
	new_string += "\x49\x45\x4E\x44\xAE\x42\x60\x82"
	f.write(new_string)

a = 3204287424
c = 1460809397
x = 2445943554

#d = open('flag.png').read()
d = string
d += '\x00' * (-len(d) % 4)
d = [d[i:i+4] for i in range(0, len(d), 4)]

e = ''
for i in range(len(d)):
	e += struct.pack('>I', x ^ struct.unpack('>I', d[i])[0])
	x = lcg(m, a, c, x)

with open('flag', 'w') as f:
	f.write(e)
	f.close()