import sqlite3
import os
class dbManager():
    def __init__(self, dbname):
        self.dbname = os.path.abspath(dbname) 
        self.conn = None
        self.cursor = None

    def open_db(self):
        self.conn = sqlite3.connect(self.dbname) 
        self.cursor = self.conn.cursor() 

    def get_books(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM book")
        data = self.cursor.fetchall()
        self.conn.close()
        
        clean_data = [tuple(str(item) for item in row) for row in data]
        
        return clean_data