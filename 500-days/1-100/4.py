def test(val, data={}):
    data[val] = val
    return data


print(test(1))
print(test(2))
