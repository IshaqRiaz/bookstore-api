from flask import Blueprint, request, jsonify
from extensions import db
from models import Book
from datetime import datetime

book_bp = Blueprint('books', __name__)


@book_bp.route('', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        price=data['price'],
        isbn=data['isbn'],
        published_date=datetime.strptime(
            data['publishedDate'], '%Y-%m-%d').date()
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id}), 201


@book_bp.route('', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': b.id, 'title': b.title, 'author': b.author,
        'price': b.price, 'isbn': b.isbn,
        'publishedDate': b.published_date.isoformat()
    } for b in books])


@book_bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id, 'title': book.title, 'author': book.author,
        'price': book.price, 'isbn': book.isbn,
        'publishedDate': book.published_date.isoformat()
    })


@book_bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.price = data.get('price', book.price)
    book.isbn = data.get('isbn', book.isbn)
    if 'publishedDate' in data:
        book.published_date = datetime.strptime(
            data['publishedDate'], '%Y-%m-%d').date()
    db.session.commit()
    return jsonify({'message': 'Updated'})


@book_bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
