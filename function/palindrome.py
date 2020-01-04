def palindrome(string):
    string2 = string[::-1]
    if string == string2: # if string = string[::-1]
        return True
    else:
        return False

name = input("enter the string : ")
print(palindrome(name))
