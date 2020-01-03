# @print_function_data
# def add(a,b):
#     return a+b

# print(add(4,5))

# output - 
# you are calling add function
# this function takes two numbers as parameter and return their sum

from functools import wraps
def print_function_data(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print(f"you are calling {any_function.__name__} function")
        print(f'{any_function.__doc__}')
        return any_function(*args, **kwargs)
    return wrapper_function

@print_function_data
def add(a, b):
    '''this function takes two numbers as parameter and return their sum'''
    return a+b

print(add(4,5))

        

