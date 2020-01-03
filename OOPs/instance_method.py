# instance method

# l = [1,2,3,4]   #object/instance of list class
# l.pop()      list.append(l,10) and l.append(10) are same       # pop-method
# print(l)

class Person:
    def __init__(a, first_name, last_name, age):  # we use self keyword for object(by convention)
        a.first_name = first_name
        a.last_name = last_name
        a.age = age
    
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"
    def full_name(self):
        return '{} {}'.format(      
            self.first_name,
            self.last_name
        )
    def is_above_18(self):
        return self.age>18


p1 = Person("pratik", "kumar", 22)
p2 = Person("Raja", "kumar", 22)

# both statement are same 
print(p2.full_name())
print(Person.full_name(p2))

print(p2.is_above_18())