from itertools import *
n_s = map(int, raw_input().rstrip().split(" "))
n = n_s[0]
s = n_s[1]
nums = map(int, raw_input().rstrip().split(" "))

count = 0

for sequence in product('01', repeat = n):
	skip = True
	for i in sequence:
		if i == '1':
			skip = False
	if not skip:
		sums = 0
		for j in range(len(sequence)):
			if sequence[j] == '1':
				sums += nums[j]
		if sums == s:
			count += 1
print(count)