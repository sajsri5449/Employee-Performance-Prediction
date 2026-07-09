# Employee Performance Prediction System

## Project Description

The Employee Performance Prediction System is a Machine Learning project that predicts whether an employee's performance is **Low, Medium, or High** based on employee details.

In this project, I collected employee data from a MySQL database, analyzed the data, trained a Machine Learning model, and created a Streamlit web application where users can enter employee details and get a predicted performance.

---

# Project Objective

The main objective of this project is to help organizations predict employee performance using Machine Learning. This can support better employee evaluation and decision-making.

---

# Dataset Information

**Dataset Name:** Employee Performance Dataset

**Total Records:** 300 Employees

**Target Column:**
- Performance

**Performance Classes:**
- Low
- Medium
- High

**Input Features Used:**
- Age
- Experience
- Training Hours
- Attendance
- Salary

---

# Technologies Used

- Python
- MySQL
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Random Forest Classifier
- Joblib
- Streamlit
- Git
- GitHub

---

# Project Workflow

## Step 1 – Connect Python with MySQL

- Connected Python to the MySQL database.
- Verified that the database connection was successful.
- Checked that the employee table was available.

---

## Step 2 – Load Data

- Loaded employee data from MySQL into a Pandas DataFrame.
- Displayed the total number of employee records.

---

## Step 3 – Understand the Dataset

- Checked the dataset structure.
- Viewed column names and data types.
- Checked for missing values.
- Checked for duplicate records.

---

## Step 4 – Load and Display Data

- Displayed the first few employee records.
- Displayed the last few employee records.
- Verified that the dataset was loaded correctly.

---

## Step 5 – Exploratory Data Analysis (EDA)

- Generated statistical information.
- Counted employees in each performance category.
- Understood the overall distribution of the data.

---

## Step 6 – Data Visualization

- Created graphs to visualize employee performance.
- Compared the number of employees in each performance category.
- Better understood the dataset visually.

---

## Step 7 – Data Preprocessing

- Converted the Performance column from text to numbers using Label Encoding.
- Selected the input features.
- Selected the target column.
- Split the dataset into training data (80%) and testing data (20%).

---

## Step 8 – Model Training

- Used the Random Forest Classifier.
- Trained the model using the training dataset.
- Evaluated the model using the testing dataset.
- Generated the accuracy score and classification report.

---

## Step 9 – Feature Importance

- Calculated the importance of each feature.
- Identified which employee attributes most influenced the prediction.
- Displayed the feature importance graph.

---

## Step 10 – Save the Model

- Saved the trained Random Forest model using Joblib.
- Saved the Label Encoder for future predictions.
- Avoided retraining the model every time the application runs.

---

## Step 11 – Test the Saved Model

- Loaded the saved model.
- Entered employee details manually.
- Predicted employee performance from the terminal.

---

## Step 12 – Build the Web Application

- Built a user-friendly web application using Streamlit.
- Users enter employee details through the interface.
- The application predicts employee performance instantly.

---

## Step 13 – Upload to GitHub

- Uploaded all project files to GitHub.
- Added project documentation.
- Added the required libraries.
- Made the project available online.

---

# Machine Learning Model

**Algorithm Used:**
Random Forest Classifier

**Model Accuracy:**
Approximately 98%

---

# Project Folder Structure

```
Employee-Performance-Prediction
│
├── app.py
├── mysql_connection.py
├── step3_dataset_info.py
├── step4_load_data.py
├── step5_eda.py
├── step6_visualization.py
├── step7_preprocessing.py
├── step8_train_model.py
├── step9_feature_importance.py
├── step10_save_model.py
├── step11_predict.py
├── employee_performance_model.pkl
├── label_encoder.pkl
├── employee_performance.csv
├── requirements.txt
└── README.md
```

---

# How to Run the Project

### Step 1

Clone the repository.

```bash
git clone <Repository Link>
```

### Step 2

Install all required libraries.

```bash
pip install -r requirements.txt
```

### Step 3

Run the Streamlit application.

```bash
python -m streamlit run app.py
```

---

# Sample Prediction

### Input

- Age = 25
- Experience = 2 Years
- Training Hours = 15
- Attendance = 85%
- Salary = 30000

### Output

```
Predicted Performance: Medium
```

---

# Future Improvements

- Connect directly to a live MySQL database.
- Deploy the application on Streamlit Cloud.
- Add user login and authentication.
- Compare Random Forest with XGBoost.
- Show prediction confidence score.
- Save prediction history.

---

# Author

**Sajal Srivastava**

B.Tech Student

Interested in Machine Learning, Data Science, Python, and Artificial Intelligence.

---

# Conclusion

This project demonstrates the complete Machine Learning workflow, including data collection, preprocessing, data analysis, visualization, model training, model evaluation, model saving, prediction, web application development, and GitHub deployment. It provides a practical example of building an end-to-end Machine Learning application for employee pe
