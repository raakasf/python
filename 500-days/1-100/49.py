def multiply(func):
	return lambda x: func(x) * 3
@multiply
def add(x):
	return x + 2
print(add(5))
