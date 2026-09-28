class Products:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.count += 1

    def get_info(self):
        print(f"Price of {self.name} is {self.price}")

    @classmethod
    def get_total_products(cls):
        print(f"Total number of products is {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"Discounted price is {price - (price * discount/100)}")


pro1 = Products("Laptop", 70_000)
pro2 = Products("Phone", 35_000)
pro3 = Products("Headphone", 2000)

pro1.get_info()
pro2.get_info()
pro3.get_info()

Products.get_total_products()

pro1.calc_discount(70_000, 25)
pro2.calc_discount(25_000, 20)
pro2.calc_discount(2000, 10)
