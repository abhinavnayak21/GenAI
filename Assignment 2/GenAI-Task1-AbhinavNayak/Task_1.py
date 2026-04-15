#Task 1: Discount Rules (if / elif / else)

order_input = input("Enter order amount: ")

# Check if input is numeric
if order_input.isdigit():
    order_amount = int(order_input)

    # Apply discount rules
    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount = 0.07
    else:
        discount = 0

    discount_amount = order_amount * discount
    subtotal = order_amount - discount_amount

    # Extra: add 5% tax
    tax = subtotal * 0.05
    final_total = subtotal + tax

    print("Original amount:", order_amount)
    print("Discount applied:", discount * 100, "%")
    print("Subtotal after discount:", subtotal)
    print("Tax (5%):", tax)
    print("Final total:", final_total)

else:
    print("Invalid input. Please enter a numeric value.")