import streamlit as st
import numpy as np
import pickle

# Load model
loaded_model = pickle.load(open('models/model.pkl', 'rb'))

# Set page configuration
st.set_page_config(page_title="Credit Card Default Prediction", page_icon=":credit_card:")

# Add custom CSS for background color
st.markdown("""
    <style>
    .reportview-container {
        background-color: #00d4ff; /* Set your background color here */
    }
    .sidebar .sidebar-content {
        background-color: #e6f7ff; /* Optional: Set background color for sidebar */
    }
    .main {
        background-color: #00d4ff; /* Apply background color to main content area */
    }
  
    </style>
""", unsafe_allow_html=True)

# Add title and description with color
st.markdown("<h1 style='color: #193c07;'>Credit Card Default Prediction</h1>", unsafe_allow_html=True)
st.write("""
This application predicts whether a credit card holder will default on their payment next month.
Please provide the following details:
""")

# Add an image
st.image("images/creditcard.jpeg", use_column_width=True)  # Replace with your image URL or file path

# Create a form to input values with colored labels
with st.form("Credit_Card_Input_Form"):
    limit_bal = st.number_input("Credit Limit", min_value=0)
    sex = st.selectbox("Gender", [1, 2], format_func=lambda x: "Male" if x == 1 else "Female")
    education = st.selectbox("Education Level", [1, 2, 3, 4], format_func=lambda x: ["Graduate School", "University", "High School", "Others"][x-1])
    marriage = st.selectbox("Marital Status", [1, 2, 3], format_func=lambda x: ["Married", "Single", "Others"][x-1])
    age = st.number_input("Age", min_value=18, step=1)
    pay_sept = st.selectbox("Repayment Status in September", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_aug = st.selectbox("Repayment Status in August", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_jul = st.selectbox("Repayment Status in July", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_jun = st.selectbox("Repayment Status in June", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_may = st.selectbox("Repayment Status in May", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    pay_apr = st.selectbox("Repayment Status in April", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    bill_amt_sept = st.number_input("Bill Amount in September", min_value=0)
    bill_amt_aug = st.number_input("Bill Amount in August", min_value=0)
    bill_amt_jul = st.number_input("Bill Amount in July", min_value=0)
    bill_amt_jun = st.number_input("Bill Amount in June", min_value=0)
    bill_amt_may = st.number_input("Bill Amount in May", min_value=0)
    bill_amt_apr = st.number_input("Bill Amount in April", min_value=0)
    pay_amt_sept = st.number_input("Payment Amount in September", min_value=0)
    pay_amt_aug = st.number_input("Payment Amount in August", min_value=0)
    pay_amt_jul = st.number_input("Payment Amount in July", min_value=0)
    pay_amt_jun = st.number_input("Payment Amount in June", min_value=0)
    pay_amt_may = st.number_input("Payment Amount in May", min_value=0)
    pay_amt_apr = st.number_input("Payment Amount in April", min_value=0)

    # Create a submit button
    form_submission = st.form_submit_button("Predict")

    # Check if the form has been submitted
    if form_submission:
        # Create a list to store the input values
        feature_values = [
            limit_bal, sex, education, marriage, age,
            pay_sept, pay_aug, pay_jul, pay_jun, pay_may, pay_apr,
            bill_amt_sept, bill_amt_aug, bill_amt_jul, bill_amt_jun, bill_amt_may, bill_amt_apr,
            pay_amt_sept, pay_amt_aug, pay_amt_jul, pay_amt_jun, pay_amt_may, pay_amt_apr
        ]

        # Reshape features for prediction
        reshaped_features = np.array(feature_values).reshape(1, -1)

        # Prediction
        prediction_result = loaded_model.predict(reshaped_features)
        predicted_default = prediction_result[0]  # Placeholder for actual prediction result

        # Display prediction result with color
        if predicted_default == 1:
            st.markdown("<h3 style='color: #FF6347;'>The credit card holder will default next month.</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color: #4CAF50;'>The credit card holder will not default next month.</h3>", unsafe_allow_html=True)
