
# Replace every element with the greatest element on right side
# if not replace with -1
# list = [16, 17, 4, 3, 5, 2]
# output = 17, 5, 5, 5, 2, -1 

# def fun(list):
#     for i in range(len(list)):
#         max = 0
#         for j in range(i+1,len(list)):
#             if list[j] > max:
#                 max = list[j]
#         if max == 0:
#             max = -1
#         list[i], max = max, list[i]
#     return list
# list = [16, 17, 4, 3, 5, 2]
# print(fun(list))


def function(list):
    for i in range(len(list)-1,0,-1):
        max = 0
        if max < list[i]:
            list[i] = max
            max = list[i]
            print(max)
        else:
            list[i] = max
    return list
list = [16, 17, 4, 3, 5, 2]
print(function(list))
        