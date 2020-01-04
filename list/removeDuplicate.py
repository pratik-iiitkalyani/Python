# method 1
# def remove_duplicate(l):
#     dic = {}
#     for i in l:
#         dic[i] = l.count(i)
#     return dic.keys()
# list = [1,2,2,3,9,9,7]
# print(remove_duplicate(list))

# method 2

# def remove_duplicate(list):
#     new_list = []
#     for i in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# list = [1,2,2,3,9,9,7]
# print(remove_duplicate(list))

# method 3 - using set 
def remove_duplicate(l):
    l = list(set(l)) 
    return l
list = [1,2,2,3,9,9,7]
print(remove_duplicate(list))



