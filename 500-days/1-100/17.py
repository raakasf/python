x = 10


def outer():
    x = 20

    # The nonlocal x statement tells Python to look for x in the nearest enclosing scope (which is outer()), rather than creating a new x in inner().
    def inner():
        nonlocal x
        x = 30

    inner()
    print(x)


outer()
print(x)
