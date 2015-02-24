#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="mysql.cs.dixie.edu", # your host, usually localhost
                     user="d0198042", # your username
                      passwd="Sanjose1", # your password
                      db="d0198042") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM items")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
