import mysql.connector as mysql

#data to be inserted as bulk
data = [
    ("Lucy", 20, 29000, "Biology"),
    ("Adam", 22, 56000, "History"),
    ("Cypher", 25, 78000, "Geography")
    ]


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
    db.execute("USE " + dbname)
    db.executemany("INSERT INTO " + dbname + " (name, age, salary, department) VALUES (%s, %s, %s, %s)", data)
    mydb.commit()
    print("Records inserted successfully")