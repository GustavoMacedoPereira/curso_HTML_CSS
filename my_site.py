from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/contacts")
def wtp():
    return render_template("contato.html")

@app.route("/Introdução")
def index():
    return render_template("index001.html")

@app.route("/Parágrafos")
def paragrafo():
    return render_template("index002.html")

@app.route("/Simbolos e emojis")
def simbols():
    return render_template("index003.html")

@app.route("/static")
def imagem():
    return render_template("index004.html")

@app.route("/favorito")
def favicon():
    return render_template("index005.html")

@app.route("/títulos")
def titulo():
    return render_template("index006.html")

@app.route("/Formatação")
def formatacao():
    return render_template("index007.html")

@app.route("/Marcação de texto")
def marca_texto():
    return render_template("index008.html")

@app.route("/outras formatações")
def other_formatation():
    return render_template("index009.html")

@app.route("/Listas")
def lista():
    return render_template("index009B.html")

@app.route("/Links")
def link():
    return render_template("index010.html")

if __name__ == "__main__":
    app.run(debug=True)
print("teste")
# Colocando o site no ar no servidor da heroku
