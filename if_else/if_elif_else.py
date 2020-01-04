# for checking multiple condition
age = int(input("enter the age: "))
if age==0 or age<0:
    print("you can't watch")
elif age > 1 and age <= 3:
    print("Ticket price : free")
elif 3<age<=10:
    print("ticket price : 150")
elif 11<age<=60:
    print("ticket price : 250")
else:
    print("ticket price: 200")