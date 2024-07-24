import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Calculator")

# Input fields for user data
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, step=1)
weight = st.number_input("Weight (in kg)", min_value=0.0, step=0.1)
height = st.number_input("Height (in meters)", min_value=0.0, step=0.01)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Hello {name}, your BMI is {bmi:.2f}.")
    else:
        st.write("Please enter a valid height.")
