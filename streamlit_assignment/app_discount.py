# Task 2: Price Calculator

import streamlit as st

st.title("Price Calculator")

# Product price input
price = st.number_input("Enter product price:", min_value=0.0)

# Discount slider
discount = st.slider("Select discount percentage:", 0, 50, 10)

# Calculate button
if st.button("Calculate"):
    final_price = price - (price * discount / 100)

    # Show result
    st.success(f"Final Price: {final_price}")

    # Extra: comparison table
    table_data = [
        ["Original Price", price],
        ["Discount (%)", discount],
        ["Final Price", final_price]
    ]

    st.table(table_data)