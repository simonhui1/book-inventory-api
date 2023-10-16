from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    author = db.Column(db.String(100), nullable = False)

@app.route('/')
def hello_world():
    return jsonify(message = "Hello, Underdog!")

@app.route('/books', methods=['GET'])
def get_books():
    search_term = request.args.get('search')
    if search_term:
        books = Book.query.filter(Book.title.like(f'%{search_term}%')).all()
    else:
        books = Book.query.all()
    output = []
    for book in books:
        book_data = {'id': book.id, 'title': book.title, 'author': book.author}
        output.append(book_data)
    return jsonify(output)


@app.route('/book', methods = ['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    new_book = Book(title = title, author = author)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(message = "Book added successfully!")

if __name__ == '__main__':
    app.run(debug = True)
