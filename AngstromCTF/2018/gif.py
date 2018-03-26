with open("/Users/ADB/Desktop/jiggs.gif", "r") as f:
	string = f.read()

print(len(string))
images = []
while "PNG" in string:
	images.append(string[string.index("PNG") - 1:string.index("IEND") + 4])
	string = string[string.index("IEND") + 1:]

with open("/Users/ADB/Desktop/random", "w") as f:
	f.write(images[0])

with open("/Users/ADB/Desktop/random2", "w") as f:
	f.write(images[1])

with open("/Users/ADB/Desktop/random3", "w") as f:
	f.write(images[2])

with open("/Users/ADB/Desktop/random4", "w") as f:
	f.write(images[3])

with open("/Users/ADB/Desktop/random5", "w") as f:
	f.write(images[4])

with open("/Users/ADB/Desktop/random6", "w") as f:
	f.write(images[5])

with open("/Users/ADB/Desktop/random7", "w") as f:
	f.write(images[6])

with open("/Users/ADB/Desktop/random8", "w") as f:
	f.write(images[7])