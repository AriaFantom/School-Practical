import mysql.connector as mysql
import pandas as pd
mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234",
)
dbname = "Teachers"
db = mydb.cursor()

db.execute("CREATE DATABASE IF NOT EXISTS " + dbname)
db.execute("USE " + dbname)

db.execute("CREATE TABLE IF NOT EXISTS " + dbname + " (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, salary INT, department VARCHAR(255))")

while True:
    print("""
    1. Insert Data
    2. Delete Record
    3. Update Record
    4. Add Data From CSV
    5. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        department = input("Enter department: ")
        db.execute("INSERT INTO " + dbname + " (name, age, salary, department) VALUES (%s, %s, %s, %s)", (name, age, salary, department))
        mydb.commit()
        print("Record inserted successfully")
    elif choice == "2":
        id = input("Enter ID to delete: ")
        db.execute("DELETE FROM " + dbname + " WHERE ID = %s", (id,))
        mydb.commit()
        print("Record deleted successfully")
    elif choice == "3":
        id = input("Enter ID to update: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        department = input("Enter department: ")
        db.execute("UPDATE " + dbname + " SET name = %s, age = %s, salary = %s, department = %s WHERE ID = %s", (name, age, salary, department, id))
        mydb.commit()
        print("Record updated successfully")
    elif choice == "4":
        filename = input("Enter file name: ")
        columns = ['name', 'age', 'salary', 'department']
        df = pd.read_csv(filename, names=columns)
        df.to_sql(dbname, mydb, if_exists='append', index=False)
        df = pd.read_sql("SELECT * FROM " + dbname, mydb)   
    elif choice == "5":
        break
    else:
        print("Invalid choice")