def add(a):
    return a**2

s = add(5)
# print(s)

s = add      # we assign add fun to var s but have not called so we can use s var as a function
print(s(7))   # --> 49 

# s and square is same 
print(s.__name__)    # --> add
print(add.__name__)    # --> add
print(s)              # memory location is same
print(add)