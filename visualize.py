import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234",
)
dbname = "Teachers"
db = mydb.cursor()
db.execute("SHOW DATABASES")

if dbname not in [x[0] for x in db.fetchall()]:
    print("Database does not exist. Please create it first with main.py")
    exit()
else:
    choice = input("Enter your choice: ")
    print("""
    1. Show the Salary as Department wise Graph
    2. Show the percentage of teachers as Department wise Pie Chart
    3. Show the slary of teacher
    4. Show all the Data from a Dataframe
    5. Search for a teacher with ID
    """)
    if choice == "1":
        db.execute("USE " + dbname)
        db.execute("SELECT department, salary FROM " + dbname)
        data = db.fetchall()
        df = pd.DataFrame(data, columns=['department', 'salary'])
        df.groupby('department').mean()['salary'].plot(kind='bar')
        plt.show()
    elif choice == "2":
        db.execute("USE " + dbname)
        db.execute("SELECT department, COUNT(*) FROM " + dbname +
                   " GROUP BY department")
        data = db.fetchall()
        departments = [x[0] for x in data]
        counts = [x[1] for x in data]
        plt.pie(counts, labels=departments, autopct="%1.1f%%")
        plt.show()
    elif choice == "3":
        db.execute("USE " + dbname)
        df = pd.read_sql("SELECT * FROM " + dbname, mydb)
        df.plot.bar(x='name', y='salary', rot=0)
        plt.show()
    elif choice == "4":
         db.execute("USE " + dbname)
         db.execute("SELECT * FROM " + dbname)
         data = db.fetchall()
         df = pd.DataFrame(data, columns=['id','name', 'age', 'salary', 'department'])
         print(df)
    elif choice == "5":
        seach = input("Enter the ID to Search: ")
        db.execute("USE " + dbname)
        db.execute("SELECT * FROM " + dbname + " WHERE id = %s", (seach,))
        data = db.fetchall()
        df = pd.DataFrame(data, columns=['id','name', 'age', 'salary', 'department'])
        print(df)
    else:
        print("Invalid choice")
