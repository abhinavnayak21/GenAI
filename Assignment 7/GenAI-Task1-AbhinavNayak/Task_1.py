# Task 1: Basic Class & Object Creation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

    # Extra: apply discount
    def apply_discount(self, percent):
        return self.price - (self.price * percent / 100)


# Create objects
p1 = Product("Laptop", 1000, "Electronics")
p2 = Product("Mouse", 50, "Accessories")

# Call method
p1.get_info()
print("Discounted price:", p1.apply_discount(10))

print()

p2.get_info()