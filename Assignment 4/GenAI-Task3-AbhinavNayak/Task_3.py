#Task 3: Append New Sales

new_sales = [5000, 2500, 1700]

# Append to file
with open("sales_data.txt", "a") as f:
    for s in new_sales:
        f.write(str(s) + "\n")

# Reopen and print updated file
with open("sales_data.txt", "r") as f:
    lines = f.readlines()

print("Updated file contents:")
for line in lines:
    print(line.strip())

# Extra: count number of lines
print("Total number of lines:", len(lines))