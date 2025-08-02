def add_entry(key, value, data={}):
    data[key] = value
    return data


print(add_entry("a", 1))
print(add_entry("b", 2))
