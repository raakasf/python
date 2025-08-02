def get_funcs():
    return [lambda x=i: x * 2 for i in range(3)]


results = [f() for f in get_funcs()]
print(results)
