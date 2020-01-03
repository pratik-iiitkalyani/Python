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
        # two ways
        # Phone.__init__(self, brand, model_name, price)   # uncomman ways
        
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


phone = Phone('Nokia', '1100', 1000)
smartphone = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}" )