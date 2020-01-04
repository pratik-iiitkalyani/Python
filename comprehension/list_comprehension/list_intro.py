# generate -ve num from 1 to 10

# list = []
# for i in range(1, 11):
#     list.append(-i)
# print(list)

# list comprehension

# negative = [-i for i in range(1,11)]
# print(negative)
#-----------------------------------

# 2nd example
# name = ['pratik', 'kumar', 'raja'] -->input
# name = ['p','k','r']

# normal method
name = ['pratik', 'kumar', 'raja']
# new_list = []
# for name in name:
#     new_list.append(name[0])
# print(new_list)

# list comprehension
name = [name[0] for name in name]
print(name)