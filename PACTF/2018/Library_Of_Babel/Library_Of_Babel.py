import zbarlight
from PIL import Image
import os

string = ""
files = []
for file in os.listdir("/Users/ADB/Desktop/qr"):
	files.append(file)
files.sort()
for file in files:
#file_path = '/Users/ADB/Desktop/coupon.png'
	with open(file, 'rb') as image_file:
	    image = Image.open(image_file)
	    image.load()
	codes = zbarlight.scan_codes('qrcode', image)
	if codes != None:
		string += codes[0]
		if "ANSWER" in codes[0]:
			print(file + "hey")
	else:
		print(file)
print(string)
	#print('QR codes: %s' % codes)
