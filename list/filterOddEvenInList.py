# input --> [1,2,3,4,5,6,7,8,9]
# output --> [[1,3,5,7,9],[2,4,6,8]]

# def func(list):
#     result = [[],[]]
#     for i in list:
#         if i%2 == 0:
#             result[1].append(i)
#         else:
#             result[0].append(i)
#     return result
# list = [1,2,3,4,5,6,7,8,9]
# print(func(list))

def func(list):
    even = []
    odd = []
    for i in list:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
        result = [odd, even]
    return result
list = [1,2,3,4,5,6,7,8,9]
print(func(list))