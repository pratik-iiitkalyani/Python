# define a function that take list of word as argument
# and return list with reverse of element in that list

# ['abc', 'tuv', 'xyz'] -----> ['cba', 'vut', 'zyx'] 

def reverseElement(l):
    result = []
    for i in l:
        result.append(i[::-1])
    return result
list = ['abc', 'tuv', 'xyz']
print(reverseElement(list))

