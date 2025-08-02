# lru_cache (Least Recently Used cache) stores results of expensive function calls and returns the cached result when the same inputs occur again. This is useful for optimizing recursive functions like Fibonacci.
from functools import lru_cache
@lru_cache(maxsize=3)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)
print(fib(5))
