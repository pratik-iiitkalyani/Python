def countList(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=1
    return count
list = [1,[2,3],[2,4,5],2]
print(countList(list))