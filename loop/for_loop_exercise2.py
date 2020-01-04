name = input("enter your name : ")
temp_var=""
i=0
for i in range(0, len(name)):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")