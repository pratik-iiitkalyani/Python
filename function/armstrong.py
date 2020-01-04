def armstrong(number):
    sum=0
    i=0
    while i<len(number):
        sum = sum+(number[i]**len(number))
        i+=1
    return (sum==number)

print(armstrong(153))
    
