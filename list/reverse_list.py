# define a which will take list containing number as input
# and return reverse list

# number = [1,2,3,4,5]
# return -------> [5,4,3,2,1]

# def reverse(l):
#     reversed_list = []
#     for i in range(len(l)):
#         reversed_list.append(l[-i-1])
#     return reversed_list
# number = [1,2,3,4,5]
# print(reverse(number))

#using only append and pop method
# def reverse(l):
#     reversed_list = []
#     for i in range(len(l)):
#         reversed_list.append(l.pop())
#     return reversed_list
# number = [1,2,3,4,5]
# print(reverse(number))

def reverse(l):
    i = 0
    j = len(l)-1
    while(i<j):
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l
number = [1,2,3,4,5]
print(reverse(number))