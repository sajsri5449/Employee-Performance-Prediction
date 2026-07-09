# 👨‍💼 Employee Performance Prediction System

## 🌐 Live Project Deployment

✅ **Streamlit Web App:**
**[https://sajsri5449-employee-performance-prediction-app-daomrh.streamlit.app/](https://sajsri5449-employee-performance-prediction-app-daomrh.streamlit.app/)**

This web application predicts an employee's performance (**Low, Medium, or High**) using a Machine Learning model based on employee details.

---

# 📌 Project Overview

Employee performance plays an important role in every organization. It helps companies identify top performers, improve employee productivity, and make better HR decisions.

This project is a Machine Learning-based Employee Performance Prediction System developed using **Python, MySQL, Scikit-learn, and Streamlit**.

The application predicts employee performance using important employee information such as age, experience, training hours, attendance, and salary.

The project also includes a Streamlit web application for real-time prediction.

---

# ❓ Problem Statement

Many organizations evaluate employee performance manually, which can be:

* Time-consuming
* Error-prone
* Difficult to analyze for a large number of employees

A Machine Learning system can analyze employee data automatically and predict employee performance quickly and consistently.

---

# 💡 My Approach (Thinking)

To solve this problem, I followed an end-to-end Machine Learning workflow:

* Connected Python with a MySQL database.
* Loaded employee data into Pandas.
* Explored and analyzed the dataset.
* Cleaned and prepared the data.
* Trained a Random Forest model.
* Evaluated the model's accuracy.
* Saved the trained model.
* Built a Streamlit web application.
* Deployed the project online using Streamlit Cloud.

---

# 🎯 Objectives

* Predict employee performance using Machine Learning.
* Analyze employee data.
* Perform data preprocessing.
* Train a classification model.
* Evaluate model accuracy.
* Build a real-time prediction system.
* Deploy the application using Streamlit.

---

# 📂 Dataset Information

**Dataset:** Employee Performance Dataset

**Total Records:** 300 Employees

**Input Features:**

* Age
* Experience
* Training Hours
* Attendance
* Salary

**Target Variable**

Employee Performance

**Classes**

* Low
* Medium
* High

---

# 🛠 Technologies Used

## Programming Language

* Python

## Database

* MySQL

## Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Streamlit
* MySQL Connector

## Platform

* VS Code
* GitHub
* Streamlit Cloud

---

# ⚙ Complete Machine Learning Workflow

## 1️⃣ MySQL Database Connection

* Connected Python with MySQL database.
* Verified successful connection.
* Accessed employee records.

---

## 2️⃣ Load Dataset

* Loaded employee data into Pandas DataFrame.
* Displayed employee records.

---

## 3️⃣ Dataset Analysis

Checked:

* Dataset shape
* Data types
* Missing values
* Duplicate values

---

## 4️⃣ Data Loading

Loaded the complete employee dataset for further analysis.

---

## 5️⃣ Exploratory Data Analysis (EDA)

Performed:

* Summary statistics
* Data understanding
* Feature analysis

---

## 6️⃣ Data Visualization

Created graphs for:

* Employee Performance
* Salary Distribution
* Attendance Distribution
* Feature Relationships

---

## 7️⃣ Data Preprocessing

Performed:

* Label Encoding
* Feature Selection
* Target Selection
* Train-Test Split (80% Training, 20% Testing)

---

## 8️⃣ Model Training

Used **Random Forest Classifier** to train the employee performance prediction model.

---

## 9️⃣ Feature Importance

Identified the most important features affecting employee performance.

---

## 🔟 Save Model

Saved:

* Trained Machine Learning Model (.pkl)
* Label Encoder (.pkl)

using Joblib.

---

## 1️⃣1️⃣ Prediction System

Loaded the saved model.

Accepted employee details from the user.

Predicted employee performance.

---

## 1️⃣2️⃣ Streamlit Web Application

Built a web application where users can:

✅ Enter employee information

✅ Predict employee performance instantly

✅ View results in a browser

---

## 1️⃣3️⃣ GitHub & Deployment

Uploaded the project to GitHub.

Deployed the application using Streamlit Cloud.

---

# 🤖 Machine Learning Model Used

## Random Forest Classifier

Random Forest is a supervised Machine Learning algorithm used for classification problems.

### Why Random Forest?

* High Accuracy
* Handles multiple features well
* Reduces overfitting
* Works well on structured datasets
* Easy to interpret using Feature Importance

---

# 📈 Model Performance

| Metric          | Result            |
| --------------- | ----------------- |
| Model Accuracy  | **98%**           |
| Prediction Type | Classification    |
| Classes         | Low, Medium, High |

---

# 🏆 Results

The developed model can successfully predict employee performance using employee information.

The system:

* Predicts performance in real time.
* Provides fast and consistent predictions.
* Achieved approximately **98% accuracy**.
* Can assist HR departments in employee evaluation.

---

# 🖥 Streamlit Web Application

The project includes a Streamlit web application where users can:

✅ Enter employee details

✅ Predict employee performance instantly

✅ Use the trained Machine Learning model through a browser

Run locally:

```bash
python -m streamlit run app.py
```

---

# 📊 Project Workflow Diagram

```
Employee Dataset
        ↓
MySQL Database
        ↓
Load Dataset
        ↓
Data Analysis
        ↓
EDA
        ↓
Visualization
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Random Forest Model
        ↓
Model Evaluation
        ↓
Feature Importance
        ↓
Save Model
        ↓
Prediction System
        ↓
Streamlit Web Application
        ↓
GitHub Deployment
```

---

# 🚀 Future Improvements

* Connect Streamlit directly with MySQL Database
* Add Login Authentication
* Add Prediction History
* Compare Multiple ML Models
* Add Explainable AI (SHAP)
* Deploy using Docker
* Create REST API using Flask/FastAPI
* Improve UI Design
* Add Employee Dashboard

---

# 📦 Installation Steps

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sajsri5449/Employee-Performance-Prediction.git
```

---

## 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Streamlit Application

```bash
python -m streamlit run app.py
```

---

# 💡 Example Prediction

### Input

Age = 25

Experience = 2 Years

Training Hours = 15

Attendance = 85%

Salary = 30000

### Output

```
Predicted Performance : Medium
```

---

# 📁 Project Structure

```
Employee-Performance-Prediction/
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
├── employee_performance.csv
├── employee_performance_model.pkl
├── label_encoder.pkl
├── requirements.txt
└── README.md
```

---

# 👨‍💻 Author

**Sajal Srivastava**

B.Tech Student

Machine Learning | Data Science | Python Developer

---

# ⭐ Key Learnings

Through this project, I learned:

* Connecting Python with MySQL
* Working with Pandas DataFrames
* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Data Visualization
* Feature Engineering
* Machine Learning Model Training
* Random Forest Classification
* Model Evaluation
* Saving Models using Joblib
* Building Streamlit Applications
* Deploying ML Projects on Streamlit Cloud
* Version Control using Git and GitHub

---

# 📌 Repository

**GitHub:**
[https://github.com/sajsri5449/Employee-Performance-Prediction](https://github.com/sajsri5449/Employee-Performance-Prediction)

---

# 🌐 Live Application

**Streamlit App:**
[https://sajsri5449-employee-performance-prediction-app-daomrh.streamlit.app/](https://sajsri5449-employee-performance-prediction-app-daomrh.streamlit.app/)

---

# ⭐ Conclusion

This project demonstrates a complete end-to-end Machine Learning pipeline, from database connectivity and data preprocessing to model training, deployment, and real-time prediction using Streamlit.

It showcases practical skills in **Python, SQL, Machine Learning, Data Analysis, GitHub, and Web App Deployment**, making it suitable for internship and placement portfolios.


