def weird_add(x):
    return lambda y: lambda z: x + y + z


print(weird_add(1)(2)(3))


print((lambda y: lambda z: 1 + y + z)(2)(3))
