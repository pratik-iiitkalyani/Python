def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return True
        return False
list = [5,7,8,72,6,4,8,1,2]
n = int(input("key:"))

if search(list,n):
    print("found")
else:
    print("not found")