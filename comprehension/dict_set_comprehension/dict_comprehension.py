# dict_comprehension
# square = {1:1,2:4,3:9}
dict = {}
for i in range(1,4):
    dict[i] = i**2
print(dict)

dict1 = {i:i**2 for i in range(1,4)}
print(dict1)

dict2 = {'square of {}'.format(i) : i**2 for i in range(1,4)}
print(dict2)

# in diffirent line
for i,j in dict2.items():
    print('{}:{}'.format(i,j))