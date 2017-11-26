import pexpect
from binascii import *
child = pexpect.spawn("nc neverending.tuctf.com 12345")
file = open("/Users/ADB/Desktop/example.txt", "r+")
child.logfile = file
child.expect("Give me some text:")
child.sendline("a")
child.expect(":")
change = 97 - int(hexlify(child.before[18]), 16)
print(change)
encrypted = child.before[29:44]
decrypted = ""
for i in encrypted:
	decrypted += chr((ord(i) + change) % 256)
child.sendline(decrypted)