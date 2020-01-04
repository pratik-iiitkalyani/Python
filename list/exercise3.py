string = ['abc','tuv','xyz']

def reverse_element(l):
    reverse = []
    for i in l:
        reverse.append(i[::-1])
    return reverse

print(reverse_element(string))