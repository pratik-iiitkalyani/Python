num1=input("enter the first num:")
num2=input("enter the 2nd num:")
total = num1+num2
print("total is " + total)
print(num1+num2)
#output: 44 bcz input fun takes the input as a string
num1=int(input("enter the first num:"))
num2=int(input("enter the 2nd num:"))
total = num1 + num2
print("total is " + "total") # then covert total into string i.e integer otherwise it cant be concated
print(num1+num2)

# str
#4 ---> "4"

#int
#"4" ---> 4

#float
# "4"--> 4.0
number1 = str(4)
number2 = float("44")
number3 = int("33")
print(number2 + number3) # float 