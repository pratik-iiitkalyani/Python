# function returning function (closure/first class function)

def outer_fun():
    def inner_fun():
        print('inside inner func')
    return inner_fun

# var = outer_fun()
# var()

def outer_fun1(msg):
    def inner_fun1():
        print(f'message is {msg}')
    return inner_fun1

var = outer_fun1('Hi Pratik')
var()