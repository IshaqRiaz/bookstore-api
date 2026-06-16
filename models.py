from extensions import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    published_date = db.Column(db.Date, nullable=False)
