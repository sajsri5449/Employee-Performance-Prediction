import streamlit as st
import pandas as pd
import joblib
# Load saved model and label encoder
model = joblib.load("employee_performance_model.pkl")
encoder = joblib.load("label_encoder.pkl")
# Title
st.title("Employee Performance Prediction System")
st.write("Enter Employee Details")
# User Input
age = st.number_input("Age", min_value=18, max_value=60, value=25)
experience = st.number_input("Experience (Years)", min_value=0, max_value=40, value=2)
training_hours = st.number_input("Training Hours", min_value=0, max_value=100, value=15)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=85)
salary = st.number_input("Salary", min_value=10000, max_value=200000, value=30000)
# Predict Button
if st.button("Predict Performance"):
    # Create DataFrame
    new_employee = pd.DataFrame({
        "Age": [age],
        "Experience": [experience],
        "Training_Hours": [training_hours],
        "Attendance": [attendance],
        "Salary": [salary]
    })
    # Predict
    prediction = model.predict(new_employee)
    # Prediction Probability
    probability = model.predict_proba(new_employee)
    confidence = probability.max() * 100
    # Convert prediction back to label
    predicted_label = encoder.inverse_transform(prediction)
    # Display Result
    st.success(f"Predicted Performance: {predicted_label[0]}")
    st.info(f"Confidence: {confidence:.2f}%")