# Task 4: Polymorphism

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(self.name, self.price)


class Laptop(Product):
    def get_info(self):
        print("Laptop:", self.name, "| Price:", self.price)


class Mobile(Product):
    def get_info(self):
        print("Mobile:", self.name, "| Price:", self.price)


# List of objects
items = [
    Laptop("Dell", 800),
    Mobile("iPhone", 1200)
]

# Polymorphism
for item in items:
    item.get_info()