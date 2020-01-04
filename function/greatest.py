# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     return c

def greater(a,b):
    if a>b:
        return a
    return b
def new_greatest(a,b,c):
    return greater(greater(a,b),c)
print(new_greatest(5,4,6))

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))
print(f"{new_greatest(num1,num2,num3)} is greatest")