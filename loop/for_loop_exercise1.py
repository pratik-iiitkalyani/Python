# practice for loop
# ask user a number like 1256 
# caculate sum of digits --->  1 + 2 + 5 + 6
number = input("enter the number : ")
sum = 0
for i in range(0, len(number)):
    sum += int(number[i])
print(sum)