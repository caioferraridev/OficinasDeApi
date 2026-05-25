from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

livros = [
    {
        "id": 1,
        "titulo": "O Hobbit",
        "autor": "J.R.R Tolkien",
        "categoria": "Fantasia",
        "descricao": "Uma aventura épica.",
        "ano": 1937,
        "avaliacao": 5,
        "imagem": "https://m.media-amazon.com/images/I/91b0C2YNSrL.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

# GET
@app.route("/livros", methods=["GET"])
def listar_livros():

    busca = request.args.get("titulo")

    if busca:
        filtrados = [
            livro for livro in livros
            if busca.lower() in livro["titulo"].lower()
        ]
        return jsonify(filtrados)

    return jsonify(livros)

# POST
@app.route("/livros", methods=["POST"])
def cadastrar_livro():

    dados = request.json

    novo_livro = {
        "id": len(livros) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "categoria": dados["categoria"],
        "descricao": dados["descricao"],
        "ano": dados["ano"],
        "avaliacao": dados["avaliacao"],
        "imagem": dados["imagem"]
    }

    livros.append(novo_livro)

    return jsonify({
        "mensagem": "Livro cadastrado!"
    })

# PUT
@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):

    dados = request.json

    for livro in livros:

        if livro["id"] == id:

            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"]
            livro["categoria"] = dados["categoria"]
            livro["descricao"] = dados["descricao"]
            livro["ano"] = dados["ano"]
            livro["avaliacao"] = dados["avaliacao"]
            livro["imagem"] = dados["imagem"]

            return jsonify({
                "mensagem": "Livro atualizado!"
            })

    return jsonify({
        "erro": "Livro não encontrado"
    }), 404

# DELETE
@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):

    global livros

    livros = [
        livro for livro in livros
        if livro["id"] != id
    ]

    return jsonify({
        "mensagem": "Livro removido!"
    })

if __name__ == "__main__":
    app.run(debug=True)