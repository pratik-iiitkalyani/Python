# list inside list
matrix = [[1,2,3],[4,5,6],[7,8,9]] # 3 list 
# print(matrix[0])

for x in matrix:
    print(x)
 
# for every element
for y in matrix:
    for x in y:
        print(x)

print(" ")
print(matrix[2][2])

print(type(matrix))