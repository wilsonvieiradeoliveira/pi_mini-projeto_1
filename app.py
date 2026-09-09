"""ByteStore: mini-projeto de Flask, Jinja2 e Bootstrap."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

@app.route("/ofertas")
def ofertas():
    return render_template("ofertas.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run()
