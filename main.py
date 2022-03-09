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
    5. Show all the Data from a Dataframe
    6. Search for a teacher with ID
    7. Exit
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
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            db.execute("INSERT INTO " + dbname + " (name, age, salary, department) VALUES (%s, %s, %s, %s)", (row['name'], row['age'], row['salary'], row['department']))
            mydb.commit()
        print("Data added successfully")
    elif choice == "5":
         db.execute("USE " + dbname)
         db.execute("SELECT * FROM " + dbname)
         data = db.fetchall()
         df = pd.DataFrame(data, columns=['id','name', 'age', 'salary', 'department'])
         print(df)
    elif choice == "6":
        seach = input("Enter the ID to Search: ")
        db.execute("USE " + dbname)
        db.execute("SELECT * FROM " + dbname + " WHERE id = %s", (seach,))
        data = db.fetchall()
        df = pd.DataFrame(data, columns=['id','name', 'age', 'salary', 'department'])
        print(df)       
    elif choice == "7":
        break
    else:
        print("Invalid choice")