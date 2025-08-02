funcs = []

for i in range(3):
    funcs.append(lambda: i)

for f in funcs:
    print(f())
