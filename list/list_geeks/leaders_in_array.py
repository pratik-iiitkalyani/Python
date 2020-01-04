# # Leaders in an array
# An element is leader if it is greater than all the elements to its right side.
#  And the rightmost element is always a leader
# array {16, 17, 4, 3, 5, 2}
# 17, 5 and 2

def leaders(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] <= list[j]:
                break
        if j == len(list)-1:
            print(list[i])
list = [16, 17, 4, 3, 5, 2]
leaders(list)


def leaders(l):
    max_element = l[-1]
    print(max_element)
    for i in range(len(list)-2, 0,-1):
        if l[i] > max_element:
            print(l[i])
            max_element = l[i]
list = [16, 17, 4, 3, 5, 2]
leaders(list)
