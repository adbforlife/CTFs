from pwn import *
import socket

data = []
with open("/Users/ADB/Desktop/Gaz_zcta_national.txt", "r") as file:
	strings = file.readlines()
	for i in range(1, len(strings)):
		data.append(strings[i].rstrip().split("\t"))
	for i in range(len(data)):
		for j in range(1, len(data[i])):
			if '.' in data[i][j]:
				data[i][j] = float(data[i][j])
			else:
				data[i][j] = int(data[i][j])
	for i in range(5):
		print(data[i])
	print(len(data))







r = remote('c1.easyctf.com', 12483)
#r.send("easy\n")
r.recv()
r.recv()
r.recv()

for n in range(51):
	question = r.recv()
	print(question)
	zip_code = question[-7:-2]
	index = 0
	for i in range(len(data)):
		if data[i][0] == zip_code:
			index = i
	answer = ""
	if "water" in question:
		answer = str(data[index][4])
	elif "land" in question:
		answer = str(data[index][3])
	elif "longitude" in question:
		answer = str(data[index][8])
	elif "latitude" in question:
		answer = str(data[index][7])
	else:
		print("wtf")

	r.send(answer + "\n")
	#print(r.recv())
r.interactive()


