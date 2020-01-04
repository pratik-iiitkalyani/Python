def binary_search(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid = (l+u)//2
        if list[mid] == n:
            return True
        else:
            if list[mid]<n:
                l = mid
            else:
                u = mid
list = [5,6,7,8,9,10,11,12,25,65,111,123]
n = int(input("key:"))

if binary_search(list,n):
    print("found")
else:
    print("not found")
