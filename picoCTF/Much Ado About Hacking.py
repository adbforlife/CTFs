original = "tuv"
bk = 0
dp = 0
dj = 0

for char in original:
    bk = ord(char)
    bk -= 32
    dj = bk
    bk = (bk + dp) % 96
    dp = dj
    bk += 32
    print(chr(bk))

resultString = "tu1|\h+&g\OP7@% :BH7M6m3g="
results = []
for char in resultString:
    results.append(ord(char))
tests = []
print(len(results))
pdp = 0
pdj = 0
dp = 0
dj = 0
bk = 0
count = 0
while not count == 26:
    for i in range(32, 127):
        bk = i
        bk -= 32
        dj = bk
        bk = (bk + dp) % 96
        dp = dj
        bk += 32
        if bk == results[count]:
            tests.append(i)
            pdp = dp
            pdj = dj
            count += 1
            break
        else:
            dp = pdp
            dj = pdj
answer = ""
for i in tests:
    answer += chr(i)
print(answer[::-1])
