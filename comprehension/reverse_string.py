# takes a list of string and return reverse of string

# normal method
def reverse(string):
    # a = list(string)
    i = 0
    j = len(string)-1
    while(i<j):
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return string
string = 'pratik'
print(reverse(string))

# def fun(l):
#     new_list = []
#     for string in range(len(l)):
#         new_list.append(reverse(string))
#     return new_list
# name = ['pratik', 'kumar', 'raja']
# print(fun(name))
