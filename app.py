from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "DevOps Handbook"},
    {"id": 2, "title": "Python for Beginners"}
]

@app.route('/')
def home():
    return "Welcome to Secure Flask App!"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

