# store any type of data
# immutable, faster then lists

#looping in tuples
mixed = (1,2,3,4,0)

for i in mixed:  # can't use while loop
    print(i)

# tuple with 1 element
nums = (1,)         #nums = (1) --not a tuple
words = ('words',)
print(type(nums))   
print(type(words))

# tuple without parenthesis

guitars = "yamaha",'taylor','baton rouge'
print(type(guitars))

#tuple unpacking
name = ("pratik",'kumar','poddar')   # element should be equal
first_name,middle_name,last_name = name  
print(first_name)

# list inside tuples
name = ("pratik",['kumar','poddar'])
# print(name[1].pop())
# print(name)
name[1].append("raja")
print(name)

# function
print(min(mixed))
print(max(mixed))
print(sum(mixed))