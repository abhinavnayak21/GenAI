# Task 1: Basic Streamlit App

import streamlit as st

# Title
st.title("Welcome to Streamlit!")

# Text input
name = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    st.write("Hello,", name)