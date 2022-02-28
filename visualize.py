import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as mysql

# connect to the database
mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234",
)
dbname = "Teachers"
db = mydb.cursor()
