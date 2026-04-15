# Task 3: Lambda Function - GST Calculator

# Lambda to add 18% GST
gst = lambda price: price + (0.18 * price)

print(gst(100))  # Expected: 118

# Extra: GST + discount together (10% discount after GST)
final_price = lambda price: (price + (0.18 * price)) * 0.90

print(final_price(100))  # Example