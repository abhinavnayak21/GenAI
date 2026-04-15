#Task 6: Read File Safely

import os

filename = input("Enter filename: ")

#Check if file exists
if os.path.exists(filename):
    with open(filename, "r") as f:
        print("\nFile contents:")
        print(f.read())
else:
    print("File not found. Please check the filename.")