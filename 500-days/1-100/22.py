def make_multipliers():
    return [lambda x: x * i for i in range(3)]


funcs = make_multipliers()
results = [f(2) for f in funcs]
print(results)
