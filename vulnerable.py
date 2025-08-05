# trigger sonarcloud scan
import sqlite3
user_input = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "'"  # SQL Injection vulnerability
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute(query)
print(cursor.fetchall())
