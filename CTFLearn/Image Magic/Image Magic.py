import Image
img = Image.new("RGB", (304, 92), (123, 123, 123))
img2 = Image.open("/Users/ADB/Desktop/out copy.png")
print(img2.getpixel((1, 0)))
for i in range(27968):
    pixel = img2.getpixel((i, 0))
    img.putpixel((i // 92, i % 92), pixel)
img.show()
