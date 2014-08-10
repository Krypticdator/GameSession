import sqlite3
class SQLController(object):
    """description of class"""
    def __init__(self):
        self.db = sqlite3.connect('data/gamedb.db')
        cursor = self.db.cursor()
        #cursor.execute('''DROP TABLE test''')
        #self.db.commit()

        cursor.execute('''CREATE TABLE IF NOT EXISTS 
        test(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, email TEXT , password TEXT)''')
        self.db.commit()

        cursor.execute('''INSERT INTO test(name, phone, email, password)
                  VALUES(?,?,?,?)''', ('john','000340', 'johndoe@butmail.com', '12345'))

        self.db.commit()

        cursor.execute('''SELECT name, email, phone FROM test''')
        user1 = cursor.fetchone() #retrieve the first row
        print(user1[0]) #Print the first column retrieved(user's name)
        all_rows = cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns email column.
            print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

        
        

    def __del__(self):
        self.db.close()



