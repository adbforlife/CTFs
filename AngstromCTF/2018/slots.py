import socket

HOST = 'web.angstromctf.com'    # The remote host
PORT = 3002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


print(s.recv(1024))
print(s.recv(1024))
while(1):
	s.send("0.01\n")
	print(s.recv(1024))
	print(s.recv(1024))
s.close()