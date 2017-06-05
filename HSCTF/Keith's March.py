with open("/Users/ADB/Desktop/adbforlife.txt", "r") as file:
    strings = file.readlines()
    xcs = []
    ycs = []
    for string in strings:
        x = string[0:string.index(" ")]
        y = string[string.index(" ") + 1: -1]
        if int(x) > 420 or int(x) < -420 or int(y) > 420 or int(y) < -420:
            xcs.append(x)
            ycs.append(y)
coordinates2 = [130, -500, -184, -500, -488, -471, -337, -487, -497, -384, -499, 78, -499, 173, -499, 308, -488, 490, -497, 381, -317, 500, 195, 498, 446, 492, 480, 489, 488, 433, 499, 123, 493, -381, 490, -431, 488, -437, 477, -466, 399, -495, 376, -498]
coordinates = [130, -500, -184, -500, -488, -471, -337, -487, -497, -384, -499, 78, -499, 308, -488, 490, -497, 381, -317, 500, 195, 498, 446, 492, 480, 489, 488, 433, 499, 123, 493, -381, 490, -431, 488, -437, 477, -466, 399, -495, 376, -498]
answer = 1
for i in coordinates:
    answer *= i
print(len(coordinates))
print(answer)
print(answer%1000000007)
