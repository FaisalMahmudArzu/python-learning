import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="faisal",
    passwd="Mahmudz26a#",
    database="telusko"
    
)

mycursor = mydb.cursor()

mycursor.execute("select * from student")



for i in mycursor:
    print(i)

