x = 100


def func():
    x = 200

    def inner():
        print(300)

    inner()
    print(x)


func()
print(x)
