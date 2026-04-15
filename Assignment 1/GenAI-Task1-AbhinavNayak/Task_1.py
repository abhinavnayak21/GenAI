#Task 1: Product Collection (List & Tuples)

#1. create a list of product
products = ["monitor", "keyboard", "Mouse", "Earphone", "Laptop", "Camera"]
sample_product = ("Laptop", 89.5, "Electronics")

#3. Print the 2nd and last product
print("2nd product:", products[1])
print("Last product:", products[-1])

#4. Append two new products and print updated list
products.append("Printer")
products.append("Desk Lamp")
print("Updated products list:", products)

#Extra (optional): Convert tuple to list, change price, and convert back to tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 69.8  # change price
sample_product = tuple(sample_product_list)

print("Updated sample product:", sample_product)