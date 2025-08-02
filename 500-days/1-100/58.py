# groupby is used to group consecutive elements in an iterable (like a list) that are the same.
from itertools import groupby

nums = [1, 1]
# k is the value being grouped (in this case, 1)
# g is a generator (iterator) over the group of matching values
groups = [(k, list(g)) for k, g in groupby(nums)]
print(groups)
