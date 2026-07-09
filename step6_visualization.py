import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
df = pd.read_sql("SELECT * FROM employee", connection)
# Performance count plot
plt.figure(figsize=(6,4))
sns.countplot(x="Performance", data=df)
plt.title("Employee Performance Distribution")
plt.show()
# Salary distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.show()
# Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.select_dtypes(include="number").corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
connection.close()