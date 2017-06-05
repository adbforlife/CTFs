file = open("/Users/ADB/Desktop/gridInfo.txt", "r")
strings = file.readlines()
file.close()
m = int(strings[0].rstrip())
n = int(strings[1].rstrip())
K = int(strings[2].rstrip())
coordinateStrings = []
for i in range(3, len(strings)):
    coordinateStrings.append(strings[i].rstrip())
coordinates = []
for i in coordinateStrings:
    xy = i.split()
    xy[0] = int(xy[0])
    xy[1] = int(xy[1])
    coordinates.append(xy)

matrix1 = [[1 for i in range(m+1)] for j in range(n+1)]
for i in coordinates:
    matrix1[i[1]][i[0]] = 0
matrix2 = []
for i in reversed(matrix1):
    matrix2.append(list(reversed(i)))
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        if matrix1[i][j] == 1 and i > 0 and j > 0:
            matrix1[i][j] = matrix1[i-1][j] + matrix1[i][j-1]
        elif i == 0 and j == 0:
            pass
        elif matrix1[i][j] == 1 and i == 0:
            matrix1[i][j] = matrix1[i][j-1]
        elif matrix1[i][j] == 1 and j == 0:
            matrix1[i][j] = matrix1[i-1][j]
for i in range(len(matrix2)):
    for j in range(len(matrix2[0])):
        if matrix2[i][j] == 1 and i > 0 and j > 0:
            matrix2[i][j] = matrix2[i-1][j] + matrix2[i][j-1]
        elif i == 0 and j == 0:
            pass
        elif matrix2[i][j] == 1 and i == 0:
            matrix2[i][j] = matrix2[i][j-1]
        elif matrix2[i][j] == 1 and j == 0:
            matrix2[i][j] = matrix2[i-1][j]

result = 0
for i in range(1, len(matrix1)):
    for j in range(len(matrix1[0])):
        result += matrix1[i][j] * matrix2[1500-i][999-j]
print((result+9512)%10000)
