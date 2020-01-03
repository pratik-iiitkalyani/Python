square = (i**2 for i in range(1, 11))
# print(next(square))
# print(next(square))

for i in square:
    print(i)

# we can loop it only once on generator
# for i in square:
#     print(i)