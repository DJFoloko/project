# app.py

import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Text input
user_input = st.text_input("Enter some text:")

# Button
if st.button("Submit"):
    st.write(f"You entered: {user_input}")

# Display some text
st.write("Welcome to my Streamlit app!")
