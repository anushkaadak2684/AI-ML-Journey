class Herbivores:
    def __init__(self, plant):
        self.plant = plant
    def eat_plant(self):
        print("Eats", self.plant)

class Carnivores:
    def __init__(self, meat):
        self.meat = meat
    def eat_meat(self):
        print("Eats", self.meat)

class Omnivores:
    def __init__(self, food):
        self.food = food
    def eat_food(self):
        print("Eats", self.plant, self.meat)

class Bear(Herbivores, Carnivores, Omnivores):
    def __init__(self, plant, meat, food):
        super().__init__(plant)
        Carnivores.__init__(self, meat)
        Omnivores.__init__(self, food)

    def sleep(self):
        print("Bear is sleeping....")

b1 = Bear("berries", "fish", "berries and fish")

b1.eat_plant()
b1.eat_meat()
b1.eat_food()
b1.sleep()