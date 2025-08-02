class MyCallable:
	def __call__(self, x):
		return x * 2
obj = MyCallable()
print(obj(3))
