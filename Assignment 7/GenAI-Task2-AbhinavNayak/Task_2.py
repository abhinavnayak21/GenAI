# Task 2: Constructor & Encapsulation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price   # private attribute
        self.category = category

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price")

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("Category:", self.category)


# Test
p = Product("Keyboard", 100, "Accessories")

p.get_info()

print("\nUpdating price...")
p.set_price(150)

print("New price:", p.get_price())

print("\nTrying invalid price...")
p.set_price(-50)