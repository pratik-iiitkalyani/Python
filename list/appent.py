# apend element in the last of the element
a = [1,2]
a.append(3)
print(a)
a.append('2')
print(a)
c = []
n = int(input('n : '))
for i in range(1,n):
    if i%2 == 0:
        c.append(i)
print(c)    