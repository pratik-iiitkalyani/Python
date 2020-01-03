# suppose we want that fun that takes only int, string or some other data type
# we have to write different function for different data type
# to avoid this we use decorator with argument

from functools import wraps

def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([(type(arg) == data_type) for arg in args]):
                return function(*args, **kwargs)
            return "invalid argument"
        return wrapper
    return decorator

@only_data_type_allow(int)
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3))

@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('pratik', 'kumar'))