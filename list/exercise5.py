list1 = [1,2,5,8]
list2 = [1,2,7,6]

def comman_element(l1,l2):
    output = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if l1[i]==l2[j]:
                output.append(l1[i])
    return output

print(comman_element(list1,list2))


def comman_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(comman_finder(list1,list2))
