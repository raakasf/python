def combine(f, g):
    return lambda x: f(g(x))


f = lambda x: x * 2
g = lambda x: x + 3

h = combine(f, g)
print(h(4))
