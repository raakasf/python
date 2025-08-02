import timeit
def test_function():
	return sum(range(100))
stmt = "test_function()"
setup = globals()
print(timeit.timeit(stmt, globals=setup, number=1000))
