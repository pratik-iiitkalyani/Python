class Person:
    # self keyword represent the object(use anything instead of self-but by 
    # convention we use self Keyword)
    def __init__(self, first_name, last_name, age):    # constructer
        print("init method is called")
        # first_name, last_name and age are the attribute of the Person class

        # instance variable

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# create object
p1 = Person("pratik", "kumar", 22)
p2 = Person("Raja", "Babu", 22)

# accesing the object
print(p1.first_name)
print(p2.first_name)