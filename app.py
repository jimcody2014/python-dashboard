import streamlit as st
import pandas as pd
import numpy as np

st.title("🧮 Simple Streamlit App Example")

# User inputs
a = st.number_input("Enter first number (a):", value=0)
b = st.number_input("Enter second number (b):", value=0)

# Add them
total = a + b
st.write(f"The sum of {a} and {b} is **{total}**.")

# Example chart
st.subheader("Random Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)
