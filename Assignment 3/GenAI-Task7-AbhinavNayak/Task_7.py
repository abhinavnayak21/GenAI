#Task 7: Menu Using Functions

#1. Add price to list
def add_price(prices_list, price):
    prices_list.append(price)


#2. Get average price
def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)


#3. Get maximum price
def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)


#Main menu
prices = []

while True:
    print("\nMenu:")
    print("1 - Add price")
    print("2 - Show average price")
    print("3 - Show highest price")
    print("q - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter price: ")

        if value.isdigit():
            add_price(prices, int(value))
            print("Price added.")
        else:
            print("Invalid input.")
            continue

    elif choice == "2":
        avg = get_average_price(prices)
        print("Average price:", avg)

    elif choice == "3":
        maximum = get_max_price(prices)
        print("Highest price:", maximum)

    elif choice == "q":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
        continue