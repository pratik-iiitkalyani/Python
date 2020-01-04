name = "      Pratik    "
dots = "................."

#lstrip()  method    for removing left space
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)  #rstrip() method for removing right space
print(name.strip() + dots)

#we can't remove space in between char
user_name="   pra   tik    "
print(user_name.strip())
# replace method

print(user_name.replace(" ",""))
