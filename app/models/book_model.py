from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    gender: Mapped[str]
    year: Mapped[int]