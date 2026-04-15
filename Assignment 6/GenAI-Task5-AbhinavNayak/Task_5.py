# Task 5: Mini Program - Safe Shopping Cart

cart = []

while True:
    value = input("Enter price (or q to quit): ")

    if value == 'q':
        break

    try:
        price = float(value)

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    except ValueError as e:
        print("Error:", e)

# Final output
print("Total items:", len(cart))
print("Total bill:", sum(cart))