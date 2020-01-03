# class variable
# cricle class
# area
# circum

class Circle:
    pi = 3.14# class variable - we have created value of pi for every object-
    #it avoid extra memory space and improve code reusebility
    def __init__(self, radius):
        self.radius = radius
        # self.pi = pi
    
    def area(self):
        return Circle.pi*self.radius*self.radius

    def circum(self):
        return 2*Circle.pi*self.radius

p1 = Circle(2)
p2 = Circle(3)
print(p1.area())
print(p2.circum())