class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        if self.age is None and self.address is None:
            print("Name:", self.name)

        elif self.address is None:
            print("Name:", self.name, "Age:", self.age)

        else:
            print("Name:", self.name, "Age:", self.age, "Address:", self.address)


p1 = Person("Anushka")
p2 = Person("Anushka", 21)
p3 = Person("Anushka", 21, "Kolkata")

p1.get_info()
p2.get_info()
p3.get_info()