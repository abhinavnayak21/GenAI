# Task 4: Mini Dashboard

import streamlit as st

# Title and description
st.title("Simple Sales Dashboard")
st.write("Monthly Sales Overview")

# Month list
months = ["January", "February", "March", "April"]

# Sales dictionary
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Select month
selected_month = st.selectbox("Select Month", months)

# Show selected month's sales
st.metric("Sales", sales[selected_month])

# Bar chart
st.bar_chart(list(sales.values()))