#Task 7: Mini Project - Export Discounted Prices

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

#ask user for discount percentage
discount_input = input("Enter discount percentage: ")

if discount_input.isdigit():
    discount_percent = int(discount_input)
    discount_rate = discount_percent / 100

    total_discounted = 0
    count = 0

    # Write to file
    with open("discount_report.txt", "w") as f:
        f.write("Product | Original Price | Discounted Price\n")

        for product in prices:
            original = prices[product]
            discounted = original - (original * discount_rate)

            total_discounted += discounted
            count += 1

            line = product + " | " + str(original) + " | " + str(discounted)
            f.write(line + "\n")

        # Extra: summary
        average = total_discounted / count
        f.write("\nTotal Items: " + str(count) + "\n")
        f.write("Average Discounted Price: " + str(average) + "\n")

    # Read and print file
    print("\nReport:\n")
    with open("discount_report.txt", "r") as f:
        print(f.read())

else:
    print("Invalid input. Please enter a number.")