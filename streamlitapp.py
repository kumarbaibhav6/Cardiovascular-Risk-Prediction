import streamlit as st
import requests

# Define the FastAPI API endpoint (change this to your EC2 instance's public IP)
api_url = "http://3.144.94.70:8000/predict"

# Title of the app
st.title('Cardiovascular Risk Prediction')

# Instructions or description of the app
st.write("Use this application to predict cardiovascular risk based on various health parameters.")

# Input fields to collect data
age = st.number_input('Age', min_value=18, max_value=120, value=45)
education = st.number_input('Education (Years)', min_value=0, max_value=20, value=12)
sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
cigs_per_day = st.number_input('Cigarettes per Day', min_value=0, max_value=100, value=20)
bp_meds = st.selectbox('Blood Pressure Medication', options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
prevalent_stroke = st.selectbox('Prevalent Stroke', options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
prevalent_hyp = st.selectbox('Prevalent Hypertension', options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
diabetes = st.selectbox('Diabetes', options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
tot_chol = st.number_input('Total Cholesterol', min_value=100, max_value=400, value=200)
bmi = st.number_input('Body Mass Index (BMI)', min_value=10, max_value=50, value=25)
heart_rate = st.number_input('Heart Rate', min_value=40, max_value=200, value=72)
glucose = st.number_input('Glucose', min_value=50, max_value=300, value=90)
map = st.number_input('Mean Arterial Pressure (MAP)', min_value=50, max_value=200, value=90)

# Prepare the data for prediction
data = {
    "age": age,
    "education": education,
    "sex": sex,
    "cigsPerDay": cigs_per_day,
    "BPMeds": bp_meds,
    "prevalentStroke": prevalent_stroke,
    "prevalentHyp": prevalent_hyp,
    "diabetes": diabetes,
    "totChol": tot_chol,
    "BMI": bmi,
    "heartRate": heart_rate,
    "glucose": glucose,
    "MAP": map
}

# Button to make prediction
if st.button('Predict'):
    # Send data to FastAPI for prediction
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        prediction = response.json()
        result = prediction.get('prediction', '')

        # Display the prediction
        if result == 1:
            st.success("Prediction: The patient has heart disease.")
            st.warning("Please consult a healthcare provider for further guidance.")
        elif result == 0:
            st.info("Prediction: The patient does not have heart disease.")
        else:
            st.error("Unexpected result. Please try again.")
    else:
        st.error("Error in prediction. Please try again.")
