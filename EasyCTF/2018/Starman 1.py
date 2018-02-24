import os
import sys
n_w = map(int, raw_input().split())
n = n_w[0]
max_weight = n_w[1]
items = []
for i in range(n):
	items.append(map(int, raw_input().split()))

answers = [[0 for i in range(max_weight + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
	for x in range(max_weight + 1):
		value = items[i - 1][0]
		weight = items[i - 1][1]
		if weight > x:
			answers[i][x] = answers[i - 1][x]
		else:
			answers[i][x] = max(answers[i - 1][x], answers[i - 1][x - weight] + value)

print(answers[n][max_weight])