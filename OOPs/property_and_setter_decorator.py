class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)  # if user give -ve price that will set to 0 
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    @property    # getter in other lang
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter                        # still we can set -ve value using _price but at least we have a better way
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

# here we can set that price -ve but practically it is not possible
# if we change that price that will not reflect in complete specification - solve by property method
# and we can change that price -ve also
phone1 = Phone('Nokia', '1100', 1000)
# print(phone1.brand)
# print(phone1.model_name)
print(phone1._price)
print(phone1.price)

phone1.price = -500
print(phone1.price)
print(phone1.complete_specification)