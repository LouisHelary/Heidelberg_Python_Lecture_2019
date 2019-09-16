import sqlite3
connection = sqlite3.connect("domoticz.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM Temperature")
result = cursor.fetchall() 

for r in result:
    print(r)