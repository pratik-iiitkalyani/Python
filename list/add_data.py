# insert method(pos, element) - add data at any position in the list
fruits = ["mango","grapes"]
fruits.insert(1,"orange")
print(fruits)

# join two list
fruits1 =[1,3]
c = fruits1+fruits   # fruits1 element come first
print(c)

#extend method
fruits.extend(fruits1)    # data of fruits1 added in fruits
print(fruits) 


fruits.append(fruits1)  # list inside list
print(fruits)
