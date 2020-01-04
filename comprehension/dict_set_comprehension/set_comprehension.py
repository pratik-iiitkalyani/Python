# Set comprehension

r = {i**2 for i in range(1,11)}
print(r)

name = ['pratik', 'kumar', 'raja']
names = {i[0] for i in name}
print(names)