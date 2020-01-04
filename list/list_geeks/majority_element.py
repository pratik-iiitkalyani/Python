# A majority element in an array A[] of size n is an element
#  that appears more than n/2 times
# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4 

# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element

def majority(l):
    max_count = 0
    for i in range(len(l)):
        count = 0        
        for j in range(len(l)):
            if i == l[j]:
                count +=1
        if count > max_count:
            max_count = count
            index = id

    if max_count> len(l)/2:
        print("majority element is {}".format(l[i]))
    else:
        print("no majority element found")
l = [1, 1, 2, 1, 3, 5, 1]
majority(l)