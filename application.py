from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name} - {self.description}"
    
class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.String(120))
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    def __repr__(self):
        return f"{self.book_name} written by {self.author} and published by {self.publisher}"

@app.route('/')
def index():
    return "Hello!"

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output =[]

    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}

        output.append(drink_data)
    return {"drinks": output}

@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'title': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return ({"name": drink.name, "description": drink.description})

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({'title': book.book_name, 'author': book.author, 'publisher': book.publisher})

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['title'],author=request.json['author'],publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return{'book successfully added'}

@app.route('/books/<id>', methods='DELETE')
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(book)
    db.session.commit
    return {"message": "it's gone"}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink():
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "it's gone"}