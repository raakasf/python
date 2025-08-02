def inner():
    yield 1
    yield 2


def outer():
    yield from inner()


print(list(outer()))
