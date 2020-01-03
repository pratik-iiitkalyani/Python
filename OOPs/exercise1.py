class Laptop:
    def __init__(self, brand, model, price):
        self.a = brand
        self.b = model
        self.c = price
        self.d = brand + " " + model

p1 = Laptop("Leneovo","anjnmj",20000)
p2 = Laptop("Hp","DKJ",56000)

print(p1.a)
print(p2.b)
print(p1.d)