import sqlite3


#Create database file
open("database.db", 'a').close()

#Create connection and cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

#Table creation queries
query_list = ["CREATE TABLE available (date text)",
              "CREATE TABLE listeners (ID INTEGER NOT NULL PRIMARY KEY, wdate text)"]

#Execute queries
for query in query_list:
    cursor.execute(query)

#Never forget to commit
connection.commit()

#Close connection
connection.close()
