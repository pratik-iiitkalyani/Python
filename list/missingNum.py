# Find the Missing Number
# nput: arr[] = {1, 2, 4,, 6, 3, 7, 8}
# Output: 5

def missingNum(l):
    n = len(l)
    sum1 = 0
    for i in l:
        sum1 += i
    sum2 = ((n+1)*(n+2))/2
    return sum2-sum1

list = [1, 2, 4, 6, 3, 7, 8]
print(missingNum(list))

