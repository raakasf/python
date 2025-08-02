def make_funcs():
    return [lambda: i for i in range(3)]


funcs = make_funcs()
results = [f() for f in funcs]
print(results)
