import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Insurance Charges Prediction App")
st.write("Enter the details below to predict insurance charges:")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# One-hot encoding for categorical variables
sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Input array
input_data = np.array([[age, bmi, children, sex_male, smoker_yes,
                        region_northwest, region_southeast, region_southwest]])

# Prediction
if st.button("Predict Charges"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:.2f}")
