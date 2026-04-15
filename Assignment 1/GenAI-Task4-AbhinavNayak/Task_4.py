# Task 4: Combined Operations

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

price_dict = {
    "Laptop": 999.99,
    "Mouse": 30.00,
    "Keyboard": 45.00,
    "Monitor": 150.75,
    "Headphones": 85.20,
    "Webcam": 60.00
}

categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Electronics"]

#1. Create catalog as list of tuples (product, price, category)
catalog = []

for i in range(len(products)):
    product = products[i]
    price = price_dict[product]
    category = categories[i]
    catalog.append((product, price, category))

print("Catalog:", catalog)

#2. Create category_to_products dictionary
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("Category to products:", category_to_products)

#3. Find category with maximum number of products
max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))

print("Category with most products:", max_category)
print("Products in that category:", category_to_products[max_category])