#Task 2: Read File in Different Ways

#Read entire file
with open("sales_data.txt", "r") as f:
    print("Using read():")
    print(f.read())

#Read 1st line
with open("sales_data.txt", "r") as f:
    print("Using readline():")
    print(f.readline())

#Read all lines and convert to integers
with open("sales_data.txt", "r") as f:
    lines = f.readlines()

#Clean and convert
numbers = []
for line in lines:
    numbers.append(int(line.strip()))

print("Using readlines() → list of integers:", numbers)