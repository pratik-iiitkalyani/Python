#delete data- pop_method(position of elememt)

a = ['mango', 'orange', 'grapes', 1, 3]
a.pop()     # delete the last element
print(a)
a.pop(0)   #print(a.pop(0))=> print the popped element
print(a)

# del operator
b = ['mango', 'orange', 'grapes', 1, 3]
del b[3]
print(b)

#remove method => remove the specified element
c = ['mango', 'orange', 'grapes', 1, 3]
# c.remove(1)
c.remove('grapes')   #if duplicate is in the list, then it will remove the first one
print(c)
