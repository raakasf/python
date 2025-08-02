from functools import lru_cache


@lru_cache()
def f(x):
    if x < 3:
        return x
    return f(x - 1) + f(x - 2)


print(f(5))
