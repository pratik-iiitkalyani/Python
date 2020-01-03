# special magic method/ dunder methods
# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    # dunder method
    # __str__, __repr__, __len__ (__str__ is preferred over __repr__)                            
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    # def __repr__(self):
    #     return f'{self.brand} {self.model} and price is {self.price}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\', \'{self.model}\', \'{self.price}\')'

    def __len__(self):
        return len(self.phone_name())

# developer use __str__ for nicely formated string and 
# __repr__ for print complete representation of the object


# l = [1,2,3]
# print(l)         # return [1, 2, 3]
my_phone = Phone('Nokia', '1100', 1000)
print(len(my_phone))
# print(my_phone)  # return the location of object in memory

# we will use dunder method to print my_phone object
print(my_phone)
# print(str(my_phone))
# print(repr(my_phone))
print(my_phone.__repr__())