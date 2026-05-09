from flask import Flask, jsonify
from services.livraria import sistema_livraria

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "preco": 29.90
    },
    {
        "id": 2,
        "titulo": "1984",
        "autor": "George Orwell",
        "preco": 49.90
    },
    {
        "id": 3,
        "titulo": "O Senhor dos Anéis",
        "autor": "J. R. R. Tolkien",
        "preco": 79.90
    }
]

@app.route("/")
def home():
    resultado = sistema_livraria(livros)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)