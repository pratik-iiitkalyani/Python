# can we drive more than one class from base class ? Yes
# multilevel inheritance
# method resolution order(MRO) - way in which python search for method and attribuites in multilevel inheritance
# method overriding
# isinstance(), issubclass()

class Phone:   # base class/ parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class Smartphone(Phone):  # derived class / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # Phone.__init__(self, brand, model_name, price)   # uncomman ways
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        # Phone.__init__(self, brand, model_name, price)   # uncomman ways
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front camera is {self.front_camera}"

# phone = Phone('Nokia', '1100', 1000)
oneplus5 = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
oneplus5t = FlagshipPhone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP', '16 MP')


print(oneplus5.full_name())
print(oneplus5t.full_name())           # method is called according to the MRO

# help(Smartphone)
# isinstance()     # check that particuler instance belong to the that particuler class, return boolean
print(isinstance(oneplus5, Smartphone))

# issubclass()     # check that particuler class is the subclass of particuler class, return boolean
print(issubclass(Smartphone, Phone))