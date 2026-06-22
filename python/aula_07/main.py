#EXERCÍCIO 1:
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Mariah Gottardo"

if __name__ == "__main__":
    app.run(debug=True)

#EXERCÍCIO 2: 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo"

@app.route("/curso")
def curso():
    return "Nome do seu curso"

@app.route("/escola")
def escola():
    return "Nome da sua escola"

if __name__ == "__main__":
    app.run(debug=True)

#EXERCÍCIO 3: 
from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Seja bem-vindo(a) à minha API!"

@app.route("/data")
def data():
    hoje = date.today()
    return f"Data de hoje: {hoje}"

if __name__ == "__main__":
    app.run(debug=True)