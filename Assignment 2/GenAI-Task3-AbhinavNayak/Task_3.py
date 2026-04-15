#Task 3: User Menu (while loop + break/continue)

orders = []

while True:
    print("\nMenu:")
    print("1 - Add order")
    print("2 - Show all orders with discounts")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        order_input = input("Enter order amount: ")

        if order_input.isdigit():
            orders.append(int(order_input))
            print("Order added.")
        else:
            print("Invalid input. Please enter a number.")
            continue

    elif choice == "2":
        if len(orders) == 0:
            print("No orders yet.")
            continue

        total_revenue = 0

        print("\nOrder Summary:")
        print("Amount -> Discount% -> Final Amount")

        for order_amount in orders:

            # Apply discount rules
            if order_amount >= 2000:
                discount = 0.15
            elif order_amount >= 1500:
                discount = 0.10
            elif order_amount >= 1000:
                discount = 0.07
            else:
                discount = 0

            final_amount = order_amount - (order_amount * discount)
            total_revenue += final_amount

            print(order_amount, "->", int(discount * 100), "% ->", final_amount)

        print("Total revenue:", total_revenue)

    elif choice == "q":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
        continue