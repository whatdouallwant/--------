import sqlite3
import os
from flask import Flask, render_template, request, redirect
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
    def create_oreder(self,book_id, user_name, phone_number, address):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO orders(book_id, user_name, phone_number, address) VALUES(?, ?, ?, ?)", [book_id, user_name, phone_number, address])
        self.conn.commit()
        self.conn.close()


    def get_books_by_price():
        max_price = request.args.get('price', default=1000, type=int)  # Отримуємо значення ціни з URL

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Фільтруємо книги за ціною
        cursor.execute("SELECT * FROM book WHERE price <= ?", (max_price,))
        books = cursor.fetchall()
        
        conn.close()

        return render_template("index.html", books=books, price_filter=max_price)
