funcs = []
for i in range(5):
    funcs.append(lambda x=i: x)

print([f() for f in funcs])
