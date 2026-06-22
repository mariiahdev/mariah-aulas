#EXERCÍCIO 1:
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def produto():

    produto = {
        "id": 1,
        "nome": "Teclado",
        "preco": 150.0,
        "disponivel": True
    }

    return jsonify(produto)

if __name__ == "__main__":
    app.run(debug=True)

#EXERCÍCIO 2:
from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado", "preco": 150.0, "disponivel": True},

    {"id": 2, "nome": "Mouse", "preco": 80.0, "disponivel": True},

    {"id": 3, "nome": "Monitor", "preco": 900.0, "disponivel": False},

    {"id": 4, "nome": "Webcam", "preco": 200.0, "disponivel": True}
]

@app.route("/produtos")
def listar_produtos():

    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)

#EXERCÍCIO 3:
from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado", "preco": 150.0, "disponivel": True},

    {"id": 2, "nome": "Mouse", "preco": 80.0, "disponivel": True},

    {"id": 3, "nome": "Monitor", "preco": 900.0, "disponivel": False},

    {"id": 4, "nome": "Webcam", "preco": 200.0, "disponivel": True}
]

@app.route("/produtos/<int:id>")
def buscar_produto(id):

    for produto in produtos:

        if produto["id"] == id:
            return jsonify(produto)

    return jsonify({"erro": "Produto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)

#EXERCÍCIO 4:
from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado", "preco": 150.0, "disponivel": True},

    {"id": 2, "nome": "Mouse", "preco": 80.0, "disponivel": True},

    {"id": 3, "nome": "Monitor", "preco": 900.0, "disponivel": False},

    {"id": 4, "nome": "Webcam", "preco": 200.0, "disponivel": True}
]

@app.route("/produtos/disponiveis")
def produtos_disponiveis():

    disponiveis = []

    for produto in produtos:

        if produto["disponivel"] == True:
            disponiveis.append(produto)

    return jsonify(disponiveis)

if __name__ == "__main__":
    app.run(debug=True)