import sqlite3

class dbManager():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None
    def get_categories(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute(''' SELECT * FROM filters''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    def open_db(self):
        self.conn = sqlite3.connect(self.dbname) 
        self.cursor = self.conn.cursor() 

    def search(self, query):
        self.open_db()
        query = '%' + query + '%'
        self.cursor.execute( ''' SELECT * FROM books WHERE (name LIKE ? OR author LIKE ?)''', [query, query])
        data = self.cursor.fetchall()
        self.conn.close()
        return data