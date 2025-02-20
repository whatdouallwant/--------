import sqlite3
import os
class dbManager():
    def __init__(self, dbname):
        self.dbname = os.path.abspath(dbname) 
        self.conn = None
        self.cursor = None
    def get_book(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute(''' SELECT * FROM book''')
        data = self.cursor.fetchall()
        self.conn.close()
        print("Дані з БД:", data)
        return data
    def open_db(self):
        self.conn = sqlite3.connect(self.dbname) 
        self.cursor = self.conn.cursor() 

    def search(self, query):
        self.open_db()
        query = '%' + query + '%'
        self.cursor.execute( ''' SELECT * FROM book WHERE (name LIKE ? OR author LIKE ?)''', [query, query])
        data = self.cursor.fetchall()
        self.conn.close()
        return data