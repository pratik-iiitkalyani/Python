# operator overloading
# polymorphism - many forms
# method overriding is also a example of polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    def __add__(self, other):              # overload + operator in our class
        return self.price + other.price

    def __mul__(self, other):              # overload * operator in our class
        return self.price * other.price

class Smartphone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"

# polymorphism - + having two different form(one is adding int and another is adding string)
# 2 + 3 = 5
# 'pratik' + ' kumar' = 'pratik kumar'

# l = [1,2,3]
# s = 'pratik
# len(l), len(s)   different form of len function


my_phone = Phone('Nokia', '1100', 1000)
my_phone2 = Phone('Nokia', '1600', 1200)
my_smartphone = Smartphone('oneplus', '5t', 33000, '26 MP')

# polymorphism because here we use two diffirent form of phone_name method
print(my_smartphone.phone_name())
print(my_phone.phone_name())


# overload +, * operator in our class 
print(my_phone + my_phone2)      
print(my_phone * my_phone2)      

