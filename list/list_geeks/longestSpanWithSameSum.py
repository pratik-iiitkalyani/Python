# Longest Span with same Sum in two Binary arrays

# Input: arr1[] = {0, 1, 0, 0, 0, 0};
#        arr2[] = {1, 0, 1, 0, 0, 1};
# Output: 4
# The longest span with same sum is from index 1 to 4.

def longestSpan(l, m, n):
    maxLen = 0
    for i in range(0, n):
        sum1 = 0
        sum2 = 0
        for j in range(i, n):
            sum1 += arr1[j]
            sum2 += arr2[j]
            if (sum1 == sum2):
                len = j-i+1
                if len > maxLen:
                    maxLen = len
    return maxLen

arr1 = [0, 1, 0, 1, 1, 1, 1] 
arr2 = [1, 1, 1, 1, 1, 0, 1]
n = len(arr1)
print(longestSpan(arr1, arr2, n))