numbers = [1,2,5,4,8,6,7,4]

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

print(square_list(numbers))

num = list(range(1,11))
print(square_list(num))