# example = [[1,2,3],[1,2,3],[1,2,3]]

example = [[i for i in range(1,4)] for i in range(1,4)]
print(example)

list1 = []
for i in range(1,4):
    list1.append(i)
list = []
for num in range(1,4):
    list.append(list1)
print(list)
