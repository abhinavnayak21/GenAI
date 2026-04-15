# Task 3: Inheritance

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(self.name, self.price, self.category)


class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    # Override method
    def get_info(self):
        print(self.name, self.price, self.category, "Warranty:", self.warranty_years, "years")


# Test
e = ElectronicProduct("Laptop", 1000, "Electronics", 2)
e.get_info()