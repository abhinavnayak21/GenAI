# Task 4: File Reader with Exception Handling

filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        lines = f.readlines()

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

else:
    print("\nFirst 3 lines:")
    for line in lines[:3]:
        print(line.strip())

finally:
    print("File operation attempted.")