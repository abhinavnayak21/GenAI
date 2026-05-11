#Task 3: Product Form

import streamlit as st

st.title("Product Form")

product_name = st.sidebar.text_input("Enter Product Name")

category = st.sidebar.selectbox(
    "Select Category",
    ["Electronics", "Accessories", "Clothing", "Books", "Home"]
)

price = st.sidebar.number_input(
    "Enter Price",
    min_value=0.0
)


if st.sidebar.button("Add Product"):

    st.success("Product Added Successfully!")

    # Display product details
    st.write("### Product Details")
    st.write("Product Name:", product_name)
    st.write("Category:", category)
    st.write("Price:", price)