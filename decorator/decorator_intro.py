# decorators - enhance the functionality of other functions
# @ - use for decorator

# whenever call the fun1 and fun2 next line will printed without changing the functionality of fun
# this is awesome function

def decorator_fun(any_fun):
    def wrapper_fun():
        print("this is awesome function")
        any_fun()
    return wrapper_fun

@decorator_fun
def fun1():
    print("this is function 1")

@decorator_fun
def fun2():
    print("this is function 2")

fun1()
fun2()

# var1 = decorator_fun(fun1)
# var1()

# fun2 = decorator_fun(fun2)
# fun2()