# ordered collection of data 
# you can store anything within list

num = [1,3,4,7,6]
print(num)

word = ["pratik","abhishek",'shashi']
print(word)

mixed = ["hfa",1,5.0, None, "amc"]
print(mixed)

#Access the list data
print(word[1])

# slicing
print(word[0:2])
print(mixed[-1]) # return last element of the list

#updation
mixed[1] = "pratik"
print(mixed)

mixed[1:] = "two"   # string will break and assinged
print(mixed)

mixed[1:] = "raja", "ankit", "pratik"
print(mixed)
