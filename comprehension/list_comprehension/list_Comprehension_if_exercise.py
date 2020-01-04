# num to string
# input--[true, false, [1,2,3],1,1.0, 3]
#output --['1', '1.0', '3']

data = [True, False, [1,2,3],1,1.0, 3]
question = [str(i) for i in data if type(i) == int or type(i)== float]
print(question)

def fun(data):
    list = []
    for i in data:
        if type(i) == int or type(i)== float:
            list.append(str(i))
    return list
print(fun(data))