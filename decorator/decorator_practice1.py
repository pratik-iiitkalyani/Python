# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total


# print(add_all(1,2,3))

# if we pass list as a argument it will throw error
# using decorator we can handle this scenario
from functools import wraps

def only_int_allowed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # data_type = []
        # for args in args:
        #     data_type.append(type(args) == int)
        # if all(data_type):
        #     return function(*args, **kwargs)
        # else:
        #     return 'Invalid argument'
        result = [(type(arg) == int) for arg in args]
        if all(result):
            return function(*args, **kwargs)
        return 'Invalid argument'
    return wrapper

@only_int_allowed
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3))