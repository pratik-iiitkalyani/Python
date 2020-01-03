# print(class_name.count_instance) - will give the number of instance created 
class Person:
    count = 0
    def __init__(self, name, age):
        Person.count += 1
        self.a = name
        self.b = age

p1 = Person('pratik', 22)
p2 = Person('raja',22)

print(Person.count)
