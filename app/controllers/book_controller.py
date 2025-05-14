from flask import request, jsonify
from app.models.book_model import Book
from app import db

def add_book():
    data = request.get_json()
    new_book = Book(**data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201