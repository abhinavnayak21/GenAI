#Task 2: Process Multiple Orders (for loop)

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discount_count = 0

print("Order Summary:")
print("Amount -> Discount% -> Final Amount")

for order_amount in orders:

    # Apply discount rules (same as Task 1)
    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount = 0.07
    else:
        discount = 0

    discount_amount = order_amount * discount
    final_amount = order_amount - discount_amount

    #Add to total revenue
    total_revenue += final_amount

    #Count orders with discount
    if discount > 0:
        discount_count += 1

    print(order_amount, "->", int(discount * 100), "% ->", final_amount)

print("\nTotal revenue after discounts:", total_revenue)

#Extra (optional)
print("Number of orders with discount:", discount_count)