class A:
    def __init__(self):
        self.val = 1

    def update(self):
        self.val += 1


a = A()
a.update()
print(a.val)
