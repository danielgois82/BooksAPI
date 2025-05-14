from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        from .models import book_model
        db.create_all()

        from .routes.book_routes import book_bp
        app.register_blueprint(book_bp)
    return app