def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

list = [2,3,4] # list is multiplied with 1 so to avoid this we have unpack the list
# list1 = *list
# print(list1)

# we can pass list and tuple both can unpack by *
print(multiply_nums(*list))