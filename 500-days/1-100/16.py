# If no custom list was passed, it uses the shared default list, which keeps getting modified across function calls.
def append_to_list(val, list=[]):
    list.append(val)
    return list


print(append_to_list(1))
print(append_to_list(2, []))
print(append_to_list(3))
