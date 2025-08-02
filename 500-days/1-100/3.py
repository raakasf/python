def choose_fn(op):
    if op == "add":
        return lambda a, b: a + b
    elif op == "mul":
        return lambda a, b: a * b


f = choose_fn("mul")
print(f(4, 5))
