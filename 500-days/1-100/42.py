from functools import reduce
import timeit
stmt = 'reduce(lambda x, y: x * y, [1, 2, 3, 4])'
print(timeit.timeit(stmt, number=1000))
