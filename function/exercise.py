def greater(a,b):
    if a>b:
        return a
    return b

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
print(f"{greater(num1,num2)} is greater")