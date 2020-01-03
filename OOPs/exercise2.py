class Laptop:
    discount = 50
    def __init__(self, brand, model, price):
        self.a = brand
        self.b = model
        self.c = price
        self.d = brand + " " + model

# if we want to change the class variable in this method--> we use self keyword
    def apply_discount(self):
        # x = (self.c*Laptop.discount)/100    # to apply static discount on every laptop
        x = (self.c*self.discount)/100        # to apply different discount on diffirent laptop
        # when we want different discount apply on different laptop
        return self.c-x

# Laptop.discount = 100                     # to change the class var 
Laptop1 = Laptop("Leneovo","anjnmj",20000)
Laptop2 = Laptop("Hp","DKJ",56000)
print(Laptop2.__dict__)

# print(Laptop1.a)
# print(Laptop2.b)
# print(Laptop1.d)

print(Laptop2.apply_discount())

Laptop1.discount = 100

# python first check object have discount if not then class var will be used
print(Laptop1.apply_discount())
print(Laptop1.__dict__)          # getting the information about object
