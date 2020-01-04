# define a fun
# input --> num, iterable(list, tuple) containing numbers as args
# example -
# num = [1,2,3]
# to_power(3, *nums)
#output -> [1,8,27]

def to_power(num, *args):
    list = []
    if len(args) == 0:
        return "hey! you didn't pass any agrs"
    else:
        return [i**num for i in args]
print(to_power(3,1,2,3))

def to_power(num, *args):
    if args:
        return [i**3 for i in args]
    else:
        return "hey! you didn't pass any agrs"
num = [1,2,3]
print(to_power(2,*num))

    