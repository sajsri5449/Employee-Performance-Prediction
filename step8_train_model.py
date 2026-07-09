import mysql.connector
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# MySQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
# Load Data
df = pd.read_sql("SELECT * FROM employee", connection)
# Encode Target
encoder = LabelEncoder()
df["Performance"] = encoder.fit_transform(df["Performance"])
# Features and Target
X = df.drop(["Employee_ID", "Performance"], axis=1)
y = df["Performance"]
# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
# Predictions
y_pred = model.predict(X_test)
# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report")
print(classification_report(y_test, y_pred))
connection.close()