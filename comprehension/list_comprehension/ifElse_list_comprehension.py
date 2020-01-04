# list comprehension with if else
# take list and return list with condition if odd return -ve num and even return multiple of 2
# input = [1,2,3,4,5,6,7,8,9,10]
# output = [-1, 2, -3, 8....]

num = list(range(1,11))
new_list = [-i if i%2 != 0 else i*2 for i in num]
print(new_list)

list = []
for i in num:
    if i%2!=0:
        list.append(-i)
    else:
        list.append(i*2)
print(list)

