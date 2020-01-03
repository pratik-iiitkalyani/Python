# generators(iterators)
# generators is also sequence like iterables

# why generators if we have list like datatype?
# memory - create space in memory(takes some time) and then memory space[.........]   - list
#          ( )           - in generators only one element is generated in one iteration 
#                             we use that num and demand for next number

# (on demand) - generators

# when to use?
# list - if we want to use that data for multiple times
# generators - single time

# generator function - yeild
# two way
# 1. generator function
# 2. generator comprehension

# inupt - 10
# output - 1...10

def fun(num):
    for i in range(1, num+1):
        # print(i)
        yield(i)   # for creating generators
    
print(fun(5))

numbers = fun(10)
for num in numbers:
    print(num)

for num in numbers:
    print(num)


# we can iterate only one times because after using the generators 
# elemant is deletes

# memory ---- 1 use that number and delete and 2 will come .......
# next num generated on demand

# we can convert generator object into list but we can loose the
# functionality of generator












