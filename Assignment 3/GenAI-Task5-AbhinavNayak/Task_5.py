#Task 5: Using filter() - Filter Expensive Products

prices = [100, 250, 400, 1200, 50, 2000, 850]

# Prices greater than 500
above_500 = list(filter(lambda p: p > 500, prices))

# Prices less than or equal to 500
below_or_equal_500 = list(filter(lambda p: p <= 500, prices))

print("Prices > 500:", above_500)
print("Prices <= 500:", below_or_equal_500)