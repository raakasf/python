# defaultdict(int) creates a dictionary where the default value for any key that doesn't exist is 0 (since int() gives 0).
from collections import defaultdict

freq = defaultdict(int)
for ch in "banana":
    freq[ch] += 1
print(freq["a"], freq["n"])
