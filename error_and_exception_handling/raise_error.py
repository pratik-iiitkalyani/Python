def add(a, b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('OOPs you are passing wrogn data type')

print(add(2, '3'))