from flask import Flask, render_template
from db_scripts import dbManager
app = Flask(__name__)
db = dbManager("templates/book.db")
@app.route("/")
def home():
    book = db.get_book()
    print("Отримані книги:", book)
    return render_template("index.html", book=book)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

if __name__ == "__main__":
    app.run(debug=True)