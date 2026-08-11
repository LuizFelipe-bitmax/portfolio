import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///estoque.db")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")

db = SQLAlchemy(app)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    produtos = db.relationship("Produto", backref="categoria", lazy=True)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)
    estoque_minimo = db.Column(db.Integer, nullable=False, default=0)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)

class Movimentacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # entrada, saída, devolução
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    produto = db.relationship("Produto", backref=db.backref("movimentacoes", lazy=True))

@app.route("/")
def index():
    produtos = Produto.query.all()
    categorias = Categoria.query.all()
    return render_template("produtos.html", produtos=produtos, categorias=categorias)

@app.route("/categorias")
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template("categorias.html", categorias=categorias)

@app.route("/categorias/add", methods=["POST"])
def add_categoria():
    nome = request.form.get("nome")
    if not nome:
        flash("Nome é obrigatório", "error")
    else:
        c = Categoria(nome=nome)
        db.session.add(c)
        db.session.commit()
        flash("Categoria adicionada", "success")
    return redirect(url_for("listar_categorias"))

@app.route("/produtos/add", methods=["POST"])
def add_produto():
    nome = request.form.get("nome")
    codigo = request.form.get("codigo")
    preco = float(request.form.get("preco") or 0)
    quantidade = int(request.form.get("quantidade") or 0)
    estoque_minimo = int(request.form.get("estoque_minimo") or 0)
    categoria_id = int(request.form.get("categoria_id") or 0)
    if not (nome and codigo and categoria_id):
        flash("Nome, código e categoria são obrigatórios", "error")
    else:
        p = Produto(
            nome=nome,
            codigo=codigo,
            preco=preco,
            quantidade=quantidade,
            estoque_minimo=estoque_minimo,
            categoria_id=categoria_id
        )
        db.session.add(p)
        db.session.commit()
        flash("Produto adicionado", "success")
    return redirect(url_for("index"))

@app.route("/produtos/delete/<int:id>")
def delete_produto(id):
    p = Produto.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    flash("Produto removido", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5001)
