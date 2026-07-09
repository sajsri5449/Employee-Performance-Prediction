import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
query = "SELECT * FROM employee"
df = pd.read_sql(query, connection)
print(df.head())
print("\nShape:", df.shape)
connection.close()