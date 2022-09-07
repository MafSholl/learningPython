class PropertyTest:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Negative amount is invalid")
        self._age = age

    @age.deleter
    def age(self):
        del self._age


pTest = PropertyTest(18)

print(pTest.age)
pTest.age = 20
print(pTest.age)
del pTest.age


