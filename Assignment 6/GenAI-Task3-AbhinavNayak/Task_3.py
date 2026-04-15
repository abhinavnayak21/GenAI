# Task 3: Custom Exception - Age Validator

def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return True


try:
    age = int(input("Enter age: "))
    check_age(age)
    print("Valid age")

except ValueError as e:
    print("Error:", e)