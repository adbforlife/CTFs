with open("/Users/ADB/Desktop/some_more_numbers.txt", "r") as f:
	nums = map(int, f.read().rstrip().split("\n"))

print(sum(nums))