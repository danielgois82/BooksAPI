from flask import Blueprint
from app.controllers import book_controller

book_bp = Blueprint("books", __name__)

book_bp.route("/books", methods=["POST"])(book_controller.add_book)

book_bp.route("/books", methods=["GET"])(book_controller.get_books)

book_bp.route("/books/<int:book_id>", methods=["GET"])(book_controller.get_book)

book_bp.route("/books/<int:book_id>", methods=["DELETE"])(book_controller.delete_book)