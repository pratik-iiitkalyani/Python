# Encapsulation
# Abstraction
# some special naming convention  
# name mangling (__name - not a convention)

# Encapsulation - Encapsulation is the process of combining data and functions into a single unit called class
# attributes of the class are kept private and public getter and setter methods are provided to
# manipulate these attributes

# abstraction - hiding the complexity from the user
# in that case user dont know how python sorted the list
# l = [3,4,1,2]  instance of list class
# l.sort()  # tim sort

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # self._price = price
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


# _name - (_ is just naming convention to tell other developer that instance var is private 
#  but developer still chnage the value) - convention of private name

# __name__ - dunder/magic method

# name mangling

phone1 = Phone('nokia', '1100', 1000)
# print(phone1.__price)    # python change __price to _Phone_price so that ensure that var belongs to Phone class
                           # but _Phone_price is still public
# phone1._price = -1100
print(phone1._Phone__price)  # we can change that one also
print(phone1.__dict__)
