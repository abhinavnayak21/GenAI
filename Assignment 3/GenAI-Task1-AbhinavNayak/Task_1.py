# Task 1: Basic Function - Price After Discount

def apply_discount(price, discount_percent=5):
    # Ensure discount does not exceed 60%
    if discount_percent > 60:
        discount_percent = 60

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


# Test cases
print(apply_discount(1000, 10))  # Expected: 900
print(apply_discount(500))       # Default 5% → 475