# Union and Intersection of two sorted arrays

# Given two sorted arrays, find their union and intersection
# Input : arr1[] = [1, 3, 4, 5, 7]
#         arr2[] = [2, 3, 5, 6]
# Output : Union : [1, 2, 3, 4, 5, 6, 7]
#          Intersection : [3, 5]

# def unionAndIntersection(list1, list2):
#     intersection = []
#     union = list1 + list2
#     for i in list1:
#         if i in list2:
#             intersection.append(i)
#     return "union: {} intersection : {}".format(sorted(set(union)), intersection)

# list1 = [1, 3, 4, 5, 7]
# list2 = [2, 3, 5, 6]
# print(unionAndIntersection(list1, list2))

def union(list1, list2):
    union = []
    i = 0
    j = 0
    while(i< len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            union.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            union.append(list2[j])
            j += 1
        else:
            union.append(list2[j])
            i += 1
            j += 1
        if len(list1) != 0:
            for i in list1:
                union.append(i)
        # while i < len(list1):
        #     print(list1[i]) 
        #     i += 1
        # while j <len(list2):
        #     print(list2[j])
        #     j += 1
    return union
list1 = [1, 3, 4, 5, 9,7,10]
list2 = [2, 3, 5, 6]
print(union(list1, list2))
        



    
