# flask --app main.py run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask import request, jsonify

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    gender: Mapped[str]
    year: Mapped[int]

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

@app.route("/teste")
def rota_teste():
    return "<p>Rota teste</p>"

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = Book(author=data["author"], gender=data["gender"], year=data["year"], title=data["title"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201

@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    result = [
        {
            "id":book.id,
            "author":book.author,
            "gender":book.gender,
            "year":book.year,
            "title":book.title
        } for book in books
    ]
    return jsonify(result)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        "id":book.id,
        "author":book.author,
        "gender":book.gender,
        "year":book.year,
        "title":book.title
    })

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.author = data.get("author", book.author)
    book.gender = data.get("gender", book.gender)
    book.year = data.get("year", book.year)
    book.title = data.get("title", book.title)

    db.session.commit()
    return jsonify({"message":"Livro atualizado com sucesso!"})

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message":"Livro removido com sucesso!"})

