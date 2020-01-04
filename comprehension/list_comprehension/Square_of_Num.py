
# with the help of list comprehension we can generate a list in one line
# create list from 1 to 10

# normal method
# def square(num):
#     list = []
#     for i in range(1, num+1):
#         list.append(i**2)
#     return list
# print(square(4))

num = 4
square_list_comprehension = [i**2 for i in range(1, num+1)]
print(square_list_comprehension)