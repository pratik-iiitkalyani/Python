# * operator solve the fix parameter problem

# def add(a,b):
#     return a+b
# print(add(1,2))  #we cant pass more then 2 parameter

# * operator solve this problem
def fun(*args):
    print(args)
    print(type(args))
fun(1,2,3,4)

def add(*args):
    total = 0
    for i in args:
        total += i
    return total
print(add(1,2,3,4))