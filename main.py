import mysql.connector as mysql

# connect to mysql
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
    4. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        department = input("Enter department: ")
        db.execute("INSERT INTO " + dbname + " (name, age, salary) VALUES (%s, %s, %s, %s)", (name, age, salary, department))
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
        break
    else:
        print("Invalid choice")

