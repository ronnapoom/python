import sqlite3
conn = sqlite3.connect(r"E:\Ronnapoom_python\example.db")
c = conn.cursor()
try :
    data = ('B','B','B'),('C','C','C'),('D','D','D')
    c.executemany('INSERT INTO users (fnme,IName,email) VALUES(?,?,?)',data)
    conn.commit()
    c.close()
except sqlite3.Error as e :
    print(e)
finally :
    if conn :
        conn.close()