# Find the minimum distance between two numbers in unsorted array
import sys
# def minDistance2(list, x, y):
#     min_dist = sys.maxsize
#     for i in range(len(list)):
#         if (list[i] == x or list[i] == y):
#             prev = i
#             break
#     for i in range(prev+1, len(list)):
#         if (list[i] == x or list[i] == y):
#             if (list[i] != list[prev]) and (i-prev)<min_dist:
#                 min_dist = i - prev 
#                 prev = i
#             else:
#                 prev = i
#     return min_dist
# arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
# print(minDistance2(arr, 3, 6))

def minDistance(list, x, y):
    min_dist = sys.maxsize
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (list[i] == x and list[j] == y) or (list[i] == j or list[j] == x) and min_dist>abs(i-j):
                min_dist = abs(i-j)
    return min_dist

        
# arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
arr = [3, 5, 4, 2, 6, 3, 0, 5, 4, 8, 3]
print(minDistance(arr, 3, 6))
            


