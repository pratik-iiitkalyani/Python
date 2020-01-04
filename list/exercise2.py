# method 1
numbers = list(range(1,11))

# def reverse_list(l):
#     reverse = numbers[::-1]     # return l[::-1]
#     return reverse

# print(reverse_list(numbers))

# method 2

# def reverse_list(l):
#     reverse = []
#     for i in l:
#         reverse.append(numbers[-i])
#     return reverse

# print(reverse_list(numbers))


# def reverse_list(l):
#     l.reverse       # return l.reverse---return none
#     return l
# print(reverse_list(numbers))



def reverse_list(l):
    r_list=[]
    for i in range(1,len(l)+1):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

print(reverse_list(numbers))