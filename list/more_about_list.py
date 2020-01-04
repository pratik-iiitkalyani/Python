# generate list with range function

# numbers = list(range(1,11))
# print(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,3,1,5,1]

print(numbers.pop())
print(numbers)

# index method
print(numbers.index(5))
print(numbers.index(1,5))
print(numbers.index(1,5,14))

# pass list to a fn

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))