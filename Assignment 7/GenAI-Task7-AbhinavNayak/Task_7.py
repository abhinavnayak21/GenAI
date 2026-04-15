# Task 7: Simple Inventory System

# Product class (reuse)
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(self.name, "|", self.price, "|", self.category)

    def __add__(self, other):
        return self.price + other.price


# Inventory class
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(name, "removed")
                return
        print("Product not found")

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

    def show_all_products(self):
        for p in self.products:
            p.get_info()


# Store class
class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        category = input("Enter category: ")

        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print("\nStore:", self.store_name)
        print("Total items:", len(self.inventory.products))
        print("Total value:", self.inventory.get_total_value())


# ---- Testing ----

store = Store("Tech Store")

# Add 3 products
for i in range(3):
    store.add_new_product()

# Show all products
print("\nProducts:")
store.inventory.show_all_products()

# Show summary
store.show_summary()

# Test __add__
if len(store.inventory.products) >= 2:
    p1 = store.inventory.products[0]
    p2 = store.inventory.products[1]
    print("\nCombined price of first two products:", p1 + p2)