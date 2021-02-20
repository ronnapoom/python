import sqlite3 #import sqlite3
conn = sqlite3.connect(r"E:\Ronnapoom_python\example.db")
c = conn.cursor() #create a cursor object 
'''c.execute (CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
   fnme varchar(30) NOT NULL,
   IName varchar(30) NOT NULL,
   email varchar(100) NOT NULL)'''
c.execute('''INSERT INTO users (id,fnme,IName,email) VALUES (NULL,"A","A","A")''')
c.execute('''INSERT INTO users VALUES (NULL,"B","B","B")''') 
conn.commit() #save (commit) the change
conn.close() #close the connecton when done 

