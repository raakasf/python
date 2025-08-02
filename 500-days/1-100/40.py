s = "abcdef"
total = 0
for i in range(0, len(s), 2):
	total += ord(s[i])
print(total)
