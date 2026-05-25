from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = [
    {
        "nome": "Caio Ferrari",
        "email": "caio@email.com",
        "telefone": "(14) 99999-1111"
    },
    {
        "nome": "Ana Souza",
        "email": "ana@email.com",
        "telefone": "(11) 98888-2222"
    },
    {
        "nome": "Carlos Lima",
        "email": "carlos@email.com",
        "telefone": "(21) 97777-3333"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usuarios")
def get_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)