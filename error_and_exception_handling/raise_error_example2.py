class Mobile:
    def __init__(self, name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        print(new_mobile)
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile class')

# we want that only object of Mobile class add mobile into mobiles list
oneplus = Mobile('one plus 6')
# print(isinstance(oneplus, Mobile))
samsung = 'samsung galaxy s8'

mobilestore = MobileStore()
print(mobilestore.mobiles)
mobilestore.add_mobile(oneplus)
print(mobilestore.mobiles[0].name)

    