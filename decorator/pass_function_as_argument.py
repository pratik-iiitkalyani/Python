# map

def square(a):
    return a**2
l = [1,2,3,4]
print(list(map(lambda a: a**2 , l)))   # map function take square as parameter(inbuilt)


# user built function taking func as parameter
def my_map(func, l):
    new_list = []
    for i in l:
        new_list.append(func(i))
    return new_list

print(my_map(square, l))
print(my_map(lambda a: a**3, l))

# using lc
def my_map1(func, l):
    return [func(i) for i in l]
print(my_map1(square, l))


