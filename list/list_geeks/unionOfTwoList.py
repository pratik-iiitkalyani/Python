# common element finder
#input -> [1,2,5,8],[1,2,7,6]
#output -> [1,2]

# takes O(n^2) time
def commonElement(l,m):
    result = []
    for i in l:
        if i in m:
            result.append(i)
    return result
list1 = [1,2,5,8]
list2 = [1,2,7,6]
print(commonElement(list1, list2))

# using set() method
# def commonElement(l,m):
#     result = list(set(l) & set(m))
#     return result
# list1 = [1,2,5,8]
# list2 = [1,2,7,6]
# print(commonElement(list1, list2))

# def commonElement(l,m):
#     result = list(set(l).intersection(m))
#     return result
# list1 = [1,2,5,8]
# list2 = [1,2,7,6]
# print(commonElement(list1, list2))