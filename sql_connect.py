import sqlite3 as sq3

db=sq3.connect("students.db")
cur=db.cursor()
cur.execute("create table stud(roll int, name varchar(20));")
result=cur.fetchall()
print(result)