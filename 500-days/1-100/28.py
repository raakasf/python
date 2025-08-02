# The reduce() function is part of the functools module. It is used to apply a binary function (a function that takes two arguments) cumulatively to the items of an iterable, from left to right, reducing the iterable to a single value.
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)
