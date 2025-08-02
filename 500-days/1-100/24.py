def adder(n):
    return lambda x: x + n


add5 = adder(5)
add10 = adder(10)
print(add5(3), add10(3))
