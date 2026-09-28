class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

c1 = Car("Toyota", "Camry", 5)
b1 = Bike("Honda", "Rebel 300", 286)

print(c1.brand, c1.model, c1.seats)
print(b1.brand, b1.model, b1.engine_cc)