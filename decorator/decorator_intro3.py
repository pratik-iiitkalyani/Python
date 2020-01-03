from functools import wraps
def decorator_fun(any_fun):
    @wraps(any_fun)
    def wrapper_fun(*args, **kwargs):
        ''' this is wrapper function'''
        print("this is awesome function")
        return any_fun(*args, **kwargs)
    return wrapper_fun


@decorator_fun
def add(a, b):
    '''this is add function'''
    return a+b

print(add.__doc__)        # --> this is wrapper function
print(add.__name__)       # --> wrapper fun because we indirectly calling the wrapper fun

# @wraps(any_fun) will solve the problem