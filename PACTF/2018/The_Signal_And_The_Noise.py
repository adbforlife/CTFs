import zlib
s = open("/Users/ADB/Desktop/download.zip", "r").read()
decoded = zlib.decompress(s)
print(s)
print("\n\n\n")
print(decoded)
print(zlib.decompress(decoded))