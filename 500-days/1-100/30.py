funcs = []
# Each time, a lambda function is created and added to the list.
# BUT: The lambda captures i by reference, not value.
# This means all the lambdas share the same i, which changes during each loop iteration.
for i in range(3):
    funcs.append(lambda: i)
results = [f() for f in funcs]
print(results)
