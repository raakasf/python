# In Python, default mutable arguments are only evaluated once, at function definition time—not each time the function is called.
def tricky(val, container={}):
    container[val] = True
    return container


print(tricky("a"))
print(tricky("b"))
