from PIL import Image
im = Image.open("/Users/ADB/Desktop/true-blue.png")
rgb_im = im.convert('RGB')
pix = rgb_im.load()
count = 0
string = ""
for j in range(128):
	for i in range(128):
		#print(rgb_im.getpixel((i,j)))
		if rgb_im.getpixel((i,j)) == (0, 49, 156):
			count += 1
			pix[i,j] = (0,0,0)
			string += "010"
		elif rgb_im.getpixel((i,j)) == (0, 49, 157):
			count += 1
			pix[i,j] = (0,0,255)
			string += "011"
		elif rgb_im.getpixel((i,j)) == (0, 48, 156):
			count += 1
			pix[i,j] = (0,255,0)
			string += "000"
		elif rgb_im.getpixel((i,j)) == (0, 48, 157):
			count += 1
			pix[i,j] = (0,255,255)
			string += "001"
		elif rgb_im.getpixel((i,j)) == (1, 49, 156):
			count += 1
			pix[i,j] = (255,0,0)
			string += "110"
		elif rgb_im.getpixel((i,j)) == (1, 49, 157):
			count += 1
			pix[i,j] = (255,0,255)
			string += "111"
		elif rgb_im.getpixel((i,j)) == (1, 48, 156):
			count += 1
			pix[i,j] = (255,255,0)
			string += "100"
		elif rgb_im.getpixel((i,j)) == (1, 48, 157):
			count += 1
			pix[i,j] = (255,255,255)
			string += "101"
		else:
			print("WTF")
print(string)
print(count)
print(rgb_im.getpixel)
rgb_im.save("true.png")