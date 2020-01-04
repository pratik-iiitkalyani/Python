# node - we cant pass *args first(*args, num) - bcoz
# *args takes all argument

def multiply_nums(num, *args): # we must pass one argument for num
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,2,3)) # first digit assign to num and remaining to *args