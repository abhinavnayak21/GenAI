#Task 3- Product Pricing (Dictionaries)

#1. Create a dictionary with at least 6 products
price_dict = {
    "Laptop": 999.99,
    "Mouse": 25.50,
    "Keyboard": 45.00,
    "Monitor": 150.75,
    "Headphones": 85.20,
    "Webcam": 60.00
}

print("Initial price dictionary:", price_dict)

#2. Add a new product
price_dict["Printer"] = 120.00
print("After adding Printer:", price_dict)

#Update price of an existing product
price_dict["Mouse"] = 30.00
print("After updating Mouse price:", price_dict)

#Remove a product (handle if not exists)
product_to_remove = "Tablet"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"{product_to_remove} removed.")
else:
    print(f"{product_to_remove} not found in dictionary.")

#3. Calculate average price
total = sum(price_dict.values())
count = len(price_dict)
average_price = total / count

print("Average price:", average_price)

#Extra (optional): product with max and min price
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive product:", max_product, "-", price_dict[max_product])
print("Cheapest product:", min_product, "-", price_dict[min_product])