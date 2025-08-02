class MyClass:
	def __init__(self, values):
		self.values = values
	# This special method allows objects of MyClass to use bracket notation (e.g., obj[1]).
	# It accesses elements of the internal self.values list by index.
	def __getitem__(self, index):
		return self.values[index]
obj = MyClass([1, 2, 3])
print(obj[1])
