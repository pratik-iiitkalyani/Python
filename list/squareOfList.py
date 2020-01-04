# define a which will take list containing number as input
# and return list containing square of every element

# number = [1,2,3,4,5]
# return -------> [1,4,9,16,25]

def squareOfElement(l):
    output = []
    for i in l:
        output.append(i*i)
    return output

number = range(1,6)
print(squareOfElement(number))
