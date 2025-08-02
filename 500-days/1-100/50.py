class Magic:
	def __bool__(self): return False
	def __len__(self): return 1
m = Magic()
print(bool(m), len(m))
