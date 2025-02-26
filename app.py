from flask import Flask, render_template, request, redirect
from db_scripts import *
app = Flask(__name__)
db = dbManager("book.db")
@app.route("/")
def home():
    search_query = request.args.get("search", "")
    genre_filter = request.args.get("genre", "all")

    books = db.get_books()
    if search_query:
        books = [book for book in books if search_query.lower() in book[0].lower() or search_query.lower() in book[1].lower()]
    if genre_filter != "all":
        books = [book for book in books if book[3].lower() == genre_filter.lower()]

    return render_template("index.html", books=books, search_query=search_query, genre_filter=genre_filter)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<int:book_id>/order", methods=["GET", "POST"])
def order(book_id):
    if request.method == "POST":
        db.create_oreder(book_id, request.form["user_name"], request.form["phone_number"], request.form["address"])
        return redirect('/')
    return render_template("order.html")
@app.route('/')
def heg():
    return get_books_by_price()


if __name__ == "__main__":
    app.run(debug=True)