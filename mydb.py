import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'jerome',
    passwd = 'password1'
)
# Prepare a cursor oject
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE jerome")

print("ALL Done!")