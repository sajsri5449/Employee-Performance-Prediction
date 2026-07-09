import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="employee_performance_db"
)
print("Connected Successfully!")
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM employee")
result = cursor.fetchone()
print("Total Employees:", result[0])
connection.close()