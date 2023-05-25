from flask import render_template, url_for
from ProjetoGaleria import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("profile.html",usuario=usuario)