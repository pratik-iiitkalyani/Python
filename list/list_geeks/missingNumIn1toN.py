# You are given a list of n-1 integers and these integers are in the range of 1 to n.
#  There are no duplicates in the list
# find missing Number

# Input: arr[] = {1, 2, 4,, 6, 3, 7, 8}
# Output: 5

def missingNumber(list):
    n = len(list)
    sum = (n+1)*(n+2)/2
    sum2 = 0
    for i in list:
        sum2+= i
    return sum-sum2
arr = [1, 2, 4, 6, 3, 7, 8]
print(missingNumber(arr))

# There can be overflow if n is large.

def getMissingNo(list):  
    i, total = 0, 1
  
    for i in range(2, len(list) + 2): 
        total += i 
        total -= list[i - 2] 
    return total 
  
# Driver Code 
arr = [1, 2, 3, 5] 
print(getMissingNo(arr))

# with XOR operation