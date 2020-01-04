num = int(input("number:"))
if num>1:   
    for i in range(2,num//2):
        if num%i == 0:
            print("not prime")
            break
    else:
            print("prime")
else:
    print(" not prime")