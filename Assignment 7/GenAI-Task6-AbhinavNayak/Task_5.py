# Task 6: Magic Methods & Operator Overloading

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # __str__ method
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator overloading
    def __add__(self, other):
        return self.price + other.price


# Test
p1 = Product("Laptop", 1000, "Electronics")
p2 = Product("Mouse", 50, "Accessories")

print(p1)  # uses __str__
print("Total price:", p1 + p2)  # uses __add__