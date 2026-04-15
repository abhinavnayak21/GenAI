# Task 6: Combined Utility Function

def process_prices(prices):
    # Apply 10% discount
    discounted_prices = list(map(lambda p: p * 0.90, prices))

    # Keep only prices above 300
    filtered_prices = list(filter(lambda p: p > 300, discounted_prices))

    return discounted_prices, filtered_prices


# Test
result = process_prices([100, 500, 900, 50, 750])

print("Discounted prices:", result[0])
print("Filtered prices (>300):", result[1])