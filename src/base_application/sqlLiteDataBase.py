import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('quintor.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS Association")

# Creating table
table = """ CREATE TABLE Association (
            AccountID STRING(35) NOT NULL PRIMARY KEY ,
            name STRING(50) NOT NULL
        ); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()