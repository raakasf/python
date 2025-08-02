def f(x, acc=[]):
    acc.append(x)
    if x > 0:
        return f(x - 1, acc)
    return sum(acc)


print(f(3))
