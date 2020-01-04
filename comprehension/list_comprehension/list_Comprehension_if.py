# list with even number in 1 to 10

def even():
    list = []
    for i in range(1, 11):
        if i%2 == 0:
            list.append(i)
    return list
print(even())

# list Comprehension
even = [i for i in range(1,11) if i%2 == 0]
odd = [i for i in range(1,11) if i%2 != 0]
print(even)
print(odd)
