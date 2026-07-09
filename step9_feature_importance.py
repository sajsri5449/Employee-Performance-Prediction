import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
# Load data
df = pd.read_sql("SELECT * FROM employee", connection)
# Encode target
encoder = LabelEncoder()
df["Performance"] = encoder.fit_transform(df["Performance"])
# Features and target
X = df.drop(["Employee_ID", "Performance"], axis=1)
y = df["Performance"]
# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)
# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})
importance = importance.sort_values(by="Importance", ascending=False)
print(importance)
# Plot
plt.figure(figsize=(8,5))
plt.bar(importance["Feature"], importance["Importance"])
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=30)
plt.show()
connection.close()