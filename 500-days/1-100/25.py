def gen():
    val = yield 1
    yield val * 2


g = gen()
print(next(g))
print(g.send(10))
