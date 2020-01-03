# class method
# difference between class method and instance method

# class method - A class method typically either creates a new instance of the class or retrieves some global properties of the class.
# Class methods do not operate on an instance or have any access to instance variable.

# instance method - instance methods operate on an object and has access to its instance variables

# 1. first argument in instance method is object and in class method is class

class Person:
    count_instance = 0 # class varaiable / class instance(same var used for every object)
    # Person.count_instance - access the class var
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

    @classmethod
    def num(cls):
        return "you have created {} instances".format(cls.count_instance)
        # return f"you have created {cls.count_instance} instances of {cls.__name__} instances"
    # we can also use Person.count_instance -> cls represent the class Person


p1 = Person("pratik", "kumar", 22)
p2 = Person("Raja", "kumar", 22)

# class method--> Person.method_name()
print(Person.num())
print(Person.count_instance)