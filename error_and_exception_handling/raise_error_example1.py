# NotImplementedError  - used in inheritance

# when call sound method of Dog and Cat class it return than same sound
# now whenever some class inherit the animal class that class has to define own sound class
# otherwise it return error
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):     #abstract method(body doesnot contain any implementation part)
        # return 'this is animal sound'
        raise NotImplementedError('you have to define this method in subclass')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meao meao'

doggy = Dog('boony', 'pug')
print(doggy.sound())