import streamlit as st
import pickle

# Function to format predicted medical cost
def format_output(cost):
    return f"Predicted Medical Cost: ${cost:.2f}"

# Main header with logo and colored title
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn4.iconfinder.com/data/icons/business-cost/64/medical-cost-health-care-hospital-512.png", width=100)  # Replace "logo.png" with the path to your logo image
with col2:
    st.markdown("<h1 style='text-align: left; color: #2980B9;'>Medical Cost Prediction</h1>", unsafe_allow_html=True)

# Add custom CSS styles
st.markdown(
    """
    <style>
        /* Add custom CSS styles */
        body {
            background-color: #f2f2f2;
        }
        .input-container, .prediction {
            background-color: #e6f7ff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            color: #2980B9; /* Set text color to blue */
        }
        .input-container h2, .prediction h3 {
            color: #2980B9; /* Set title color to blue */
        }
        .footer {
            margin-top: 20px;
            font-size: 14px;
            color: #777;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Input form container
st.markdown("<div class='input-container'><h2 style='color: #2980B9;'>Input Parameters</h2></div>", unsafe_allow_html=True)

with st.form("medical_cost_prediction_form"):
    age = st.number_input("Age", min_value=0, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)
    children = st.number_input("Number of Children", min_value=0, step=1)
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    region = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])

    submitted = st.form_submit_button("Predict Medical Cost")

# Main content area
if submitted:
    if age != 0 and bmi != 0.0:
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
        st.markdown("<div class='prediction'><h3>Prediction Result</h3><p>" + format_output(output[0]) + "</p></div>", unsafe_allow_html=True)
    else:
        st.error("Please enter all input parameters.")
