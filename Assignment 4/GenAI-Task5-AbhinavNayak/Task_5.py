#Task 5: Create Product Info File (User Input)

#Take input for 3 products
products = []

for i in range(3):
    name = input("Enter product name: ")
    price = input("Enter price: ")
    products.append(name + " | " + price)

#Write to file
with open("products.txt", "w") as f:
    for p in products:
        f.write(p + "\n")

#Read and print
print("\nProduct List:")
with open("products.txt", "r") as f:
    for line in f:
        parts = line.strip().split("|")
        print("Product:", parts[0].strip(), "- Price:", parts[1].strip())