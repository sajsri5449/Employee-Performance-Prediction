import mysql.connector
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
df = pd.read_sql("SELECT * FROM employee", connection)
encoder = LabelEncoder()
df["Performance"] = encoder.fit_transform(df["Performance"])
X = df.drop(["Employee_ID", "Performance"], axis=1)
y = df["Performance"]
model = RandomForestClassifier(random_state=42)
model.fit(X, y)
joblib.dump(model, "employee_performance_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")
print("Model Saved Successfully!")
connection.close()