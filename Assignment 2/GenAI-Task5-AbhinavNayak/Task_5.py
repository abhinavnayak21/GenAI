#Task 5: Loop Control with Conditions (break & continue)

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    #If corrupted data, stop loop
    if sale == -1:
        print("Corrupted data found. Stopping...")
        break

    #If no sales, skip
    if sale == 0:
        print("No sales today. Skipping...")
        continue

    #Add valid sales
    total_sales += sale
    print("Added:", sale, "| Running total:", total_sales)

#Final total
print("Final total sales:", total_sales)