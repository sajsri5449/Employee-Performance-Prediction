import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
df = pd.read_sql("SELECT * FROM employee", connection)
print("\nDataset Information:")
print(df.info())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
connection.close()