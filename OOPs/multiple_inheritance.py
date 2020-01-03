# multiple inheritance

class A:

    def class_a_method(self):
        return 'I\'m just a class A method'

    def hello(self):
        return 'hello from class A'

class B:

    def class_b_method(self):
        return 'I\'m just a class B method'

    def hello(self):
        return 'hello from class B'

class C(A, B):      # method and instance will search by according to the parameter order
    pass

# instance_a = A()
# print(instance_a.class_a_method())
instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())     # hello method of class A will be return

# help(C)
# print(C.mro())                # return list of class 
# print(C.__mro__)              # return tuple of class