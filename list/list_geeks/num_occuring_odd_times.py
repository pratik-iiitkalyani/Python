# Find the Number Occurring Odd Number of 
# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3  --> Only one element will exist

def function(list):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = list.count(list[i])
    for i in dict:
        if dict[i]%2 != 0:
            return i
    return "no such elemnt"


list = [1, 2, 3, 2, 3, 1, 3]
print(function(list))

# using loop --> 0(n*n)
def fun(list):
    for i in list:
        count = 0
        for j in range(len(list)):
            if i == list[j]:
                count += 1
        if count%2 != 0:
            return i
list = [1, 2, 3, 2, 3, 1, 3]
print(fun(list))