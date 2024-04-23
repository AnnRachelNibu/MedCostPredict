import streamlit as st
import pickle

st.header("Medical Cost Prediction")

with st.form("medical_cost_prediction_form"):
    age = st.number_input("Enter age")
    sex = st.selectbox("Select sex", ["Male", "Female"])
    bmi = st.number_input("Enter BMI")
    children = st.number_input("Enter number of children")
    smoker = st.selectbox("Smoker?", ["Yes", "No"])
    region = st.selectbox("Select region", ["Southwest", "Southeast", "Northwest", "Northeast"])

    submitted = st.form_submit_button("Predict Medical Cost")

if submitted:
        # Convert input values to appropriate format
        sex = 1 if sex == "Male" else 0
        smoker = 1 if smoker == "Yes" else 0
        region_encoded = [0, 0, 0, 0]  # initialize all regions as 0
        region_index = ["Southwest", "Southeast", "Northwest", "Northeast"].index(region)
        region_encoded[region_index] = 1  # set the selected region to 1

        # Prepare input data for prediction
        input_data = [[age, sex, bmi, children, smoker] + region_encoded]

        # Load the trained model
        with open("medical_model.dat", "rb") as f:
            model = pickle.load(f)

        # Make prediction
        output = model.predict(input_data)

        # Display prediction
        st.write(f"The predicted medical cost is: {float(output[0])}")