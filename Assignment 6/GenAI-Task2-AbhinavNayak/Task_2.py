# Task 2: Bill Calculator with Error Handling

prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for p in prices:
    try:
        # Check type
        if not isinstance(p, (int, float)):
            raise TypeError

        # Check negative
        if p < 0:
            raise ValueError("Negative price not allowed")

        total += p
        print("Added:", p, "| Running total:", total)

    except TypeError:
        print("Invalid type:", p)

    except ValueError as e:
        print(e)

print("Final total:", total)