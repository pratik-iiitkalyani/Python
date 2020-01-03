# if we pass some arugument in fun1 it gives error because wrapper function is not taking argument
# to resolve this we pass *args and **kwargs in wrapper_fun

def decorator_fun(any_fun):
    def wrapper_fun(*args, **kwargs):
        print("this is awesome function")
        return any_fun(*args, **kwargs)
    return wrapper_fun

@decorator_fun
def fun1(a):
    print(f"this is function with argument {a}")

fun1(8)

@decorator_fun
def add(a, b):
    return a+b

print(add(2,3))
# it will not return a+b because we not returning any fun