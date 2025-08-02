class MyClass:
	def __init__(self, x):
			self.x = x
	def __call__(self, y):
		return self.x + y
obj = MyClass(10)
print(obj(5))
