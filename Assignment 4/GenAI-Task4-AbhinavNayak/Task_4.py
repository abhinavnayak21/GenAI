#Task 4: Generate Summary Report from File

#Read file and convert to integers
with open("sales_data.txt", "r") as f:
    lines = f.readlines()

sales = []
for line in lines:
    sales.append(int(line.strip()))

#Calculate values
total = sum(sales)
highest = max(sales)
lowest = min(sales)
average = total / len(sales)

#Print results
print("Total Sales:", total)
print("Highest Sale:", highest)
print("Lowest Sale:", lowest)
print("Average Sale:", average)