# Task 2: Recursive Function - Factorial Utility

def factorial(n):
    # Handle negative input
    if n < 0:
        print("Error: Negative number")
        return None

    # Base cases
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Test cases
print("factorial(5):", factorial(5))
print("factorial(0):", factorial(0))
print("factorial(-3):", factorial(-3))