list = [1,2,3,[1,2]]

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=1
    return count

print(sublist_counter(list))