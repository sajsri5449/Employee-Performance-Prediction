import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
df = pd.read_sql("SELECT * FROM employee", connection)
print("First 10 Rows")
print(df.head(10))
print("\nLast 10 Rows")
print(df.tail(10))
print("\nStatistical Summary")
print(df.describe())
print("\nPerformance Value Counts")
print(df["Performance"].value_counts())
connection.close()