n = input("enter the number with more then one digit:")
total = 0
i = 0
while i<len(n):
    total += int(n[i])
    i = i+1
print(total)
