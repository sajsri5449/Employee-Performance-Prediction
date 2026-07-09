# Employee Performance Prediction System

## Live Demo

🚀 Streamlit App  
https://sajsri5449-employee-performance-prediction-app-daomrh.streamlit.app/

📂 GitHub Repository  
https://github.com/sajsri5449/Employee-Performance-Prediction

---

# Problem Statement

Many organizations evaluate employee performance manually.

This process takes time, may contain human errors, and becomes difficult when there are many employees.

The goal of this project is to use Machine Learning to predict employee performance automatically from employee information.

---

# Solution

I developed an end-to-end Machine Learning application that predicts whether an employee's performance is:

- Low
- Medium
- High

The user enters employee details into a Streamlit web application, and the trained Machine Learning model predicts the employee's performance instantly.

---

# Project Features

✔ Employee Performance Prediction

✔ Interactive Streamlit Web Application

✔ MySQL Database Integration

✔ Data Analysis using Pandas

✔ Exploratory Data Analysis (EDA)

✔ Data Visualization

✔ Machine Learning Model Training

✔ Feature Importance Analysis

✔ Model Saving using Joblib

✔ Real-time Prediction

✔ GitHub Version Control

✔ Live Deployment on Streamlit Cloud

---

# Project Workflow

### Step 1 - Connect MySQL Database
- Connected Python with MySQL.
- Retrieved employee records from the database.

### Step 2 - Load Dataset
- Loaded employee data into a Pandas DataFrame.

### Step 3 - Understand the Dataset
- Checked data types.
- Checked missing values.
- Checked duplicate records.
- Viewed dataset information.

### Step 4 - Data Loading
- Loaded all employee records successfully.

### Step 5 - Exploratory Data Analysis
- Analyzed employee data.
- Understood feature distributions.
- Generated summary statistics.

### Step 6 - Data Visualization
Created graphs for:
- Performance Distribution
- Salary Distribution
- Attendance Distribution

### Step 7 - Data Preprocessing
- Label Encoding
- Feature Selection
- Train-Test Split

### Step 8 - Model Training
Trained a Random Forest Classifier using employee data.

### Step 9 - Feature Importance
Identified which employee features have the highest impact on performance prediction.

### Step 10 - Save Model
Saved the trained Machine Learning model and Label Encoder using Joblib.

### Step 11 - Prediction
Accepted employee details from the user and predicted performance.

### Step 12 - Streamlit Web Application
Built an interactive web application where users can predict employee performance instantly.

### Step 13 - GitHub & Deployment
Uploaded the complete project to GitHub and deployed it on Streamlit Cloud.

---

# Dataset

Dataset Name

Employee Performance Dataset

Total Records

300 Employees

Input Features

- Age
- Experience
- Training Hours
- Attendance
- Salary

Target

Performance

Output Classes

- Low
- Medium
- High

---

# Technologies Used

### Programming

- Python

### Database

- MySQL

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib

### Machine Learning

- Scikit-Learn
- Random Forest Classifier

### Model Saving

- Joblib

### Web Application

- Streamlit

### Version Control

- Git
- GitHub

### Deployment

- Streamlit Community Cloud

---

# Machine Learning Pipeline

```
MySQL Database
        │
        ▼
Load Dataset
        │
        ▼
Data Cleaning
        │
        ▼
EDA
        │
        ▼
Visualization
        │
        ▼
Preprocessing
        │
        ▼
Random Forest Model
        │
        ▼
Save Model
        │
        ▼
Streamlit App
        │
        ▼
Prediction
```

---

# Model Performance

Machine Learning Algorithm

Random Forest Classifier

Accuracy

98%

Prediction Classes

- Low
- Medium
- High

---

# Sample Prediction

### Input

Age = 25

Experience = 2 Years

Training Hours = 15

Attendance = 85%

Salary = 30000

### Output

```
Predicted Performance: Medium
```

---

# Project Structure

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

# How to Run

Clone Repository

```bash
git clone https://github.com/sajsri5449/Employee-Performance-Prediction.git
```

Install Libraries

```bash
pip install -r requirements.txt
```

Run Application

```bash
python -m streamlit run app.py
```

---

# Live Demo

Try the application here:

**https://sajsri5449-employee-performance-prediction-app-daomrh.streamlit.app/**

---

# Skills Demonstrated

- Python Programming
- SQL & MySQL
- Data Analysis
- Exploratory Data Analysis
- Data Visualization
- Machine Learning
- Random Forest
- Feature Engineering
- Model Evaluation
- Model Serialization
- Streamlit Development
- Git & GitHub
- Project Deployment

---

# Future Improvements

- User Login System
- Admin Dashboard
- Prediction History
- Direct MySQL Integration in Streamlit
- Multiple ML Model Comparison
- XGBoost Implementation
- Explainable AI (SHAP)
- REST API using FastAPI
- Docker Deployment
- Cloud Database Integration

---

# About Me

**Sajal Srivastava**

B.Tech Student

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer

---

