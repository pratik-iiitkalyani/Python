class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):   # instance method
        return '{} {}'.format(      
            self.first_name,
            self.last_name
        )
    def is_above_18(self):
        return self.age>18

    # static method
    @staticmethod
    def hello():
        print("hello")

    @classmethod
    def num(cls):
        return "you have created {} instances".format(cls.count_instance)

    # class method as a constructor
    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(",")
        return cls(first, last, age)


p1 = Person("pratik", "kumar", 22)
p2 = Person("Raja", "kumar", 22)

# class method--> Person.method_name()
p3 = Person.from_string("pratik,kumar,age")
# acceessing the class method
print(p3.first_name)

# calling the static method
Person.hello()
