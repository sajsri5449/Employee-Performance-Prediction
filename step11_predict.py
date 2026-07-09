import joblib
import pandas as pd
# Load saved model and encoder
model = joblib.load("employee_performance_model.pkl")
encoder = joblib.load("label_encoder.pkl")
print("Employee Performance Prediction")
# Take input from user
age = int(input("Enter Age: "))
experience = int(input("Enter Experience (Years): "))
training_hours = int(input("Enter Training Hours: "))
attendance = int(input("Enter Attendance (%): "))
salary = int(input("Enter Salary: "))
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
# Convert number back to label
result = encoder.inverse_transform(prediction)
print("\nPredicted Performance:", result[0])