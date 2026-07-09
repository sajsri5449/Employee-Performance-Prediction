import mysql.connector
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# MySQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
# Load Data
df = pd.read_sql("SELECT * FROM employee", connection)
print("Original Dataset")
print(df.head())
# Encode Target Column
label_encoder = LabelEncoder()
df["Performance"] = label_encoder.fit_transform(df["Performance"])
print("\nAfter Label Encoding")
print(df.head())
# Features and Target
X = df.drop(["Employee_ID", "Performance"], axis=1)
y = df["Performance"]
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
connection.close()