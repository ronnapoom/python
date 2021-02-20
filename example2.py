import sqlite3

def insertTousers(fnme,IName,email) :
    try :
        conn = sqlite3.connect(r"E:\Ronnapoom_python\example.db")
        c = conn.cursor()

        sql = ''' INSERT INTO users (fnme,IName,email) VALUES (?,?,?) '''
        data = (fnme,IName,email)
        c.execute(sql,data)
        conn.commit ()
        c.close ()

    except sqlite3.Error as e :
        print('Failed to insert : ',e)
    finally :
        conn.close ()

insertTousers('Guido','Rossum','python@gmail.com')
insertTousers('Dennis','Ritchie','abc')

