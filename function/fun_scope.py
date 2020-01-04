x=7    #global var
def fun():
    x=5   # local var...can't accessable outside the fn
    return x
print(fun())
# print(x)    gives error