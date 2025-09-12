
import os
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///agendamentos.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-change-me')

db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    duracao = db.Column(db.Integer, default=60)  

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'), nullable=False)
    inicio = db.Column(db.DateTime, nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('agendamentos', lazy=True))
    servico = db.relationship('Servico', backref=db.backref('agendamentos', lazy=True))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.order_by(Cliente.nome).all()
    return render_template('clientes.html', clientes=clientes)

@app.route('/clientes/add', methods=['POST'])
def add_cliente():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    email = request.form.get('email')
    if not nome:
        flash('Nome é obrigatório', 'error')
        return redirect(url_for('listar_clientes'))
    c = Cliente(nome=nome, telefone=telefone, email=email)
    db.session.add(c)
    db.session.commit()
    flash('Cliente adicionado', 'success')
    return redirect(url_for('listar_clientes'))

@app.route('/clientes/delete/<int:id>')
def delete_cliente(id):
    c = Cliente.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash('Cliente removido', 'success')
    return redirect(url_for('listar_clientes'))


@app.route('/servicos')
def listar_servicos():
    servicos = Servico.query.order_by(Servico.nome).all()
    return render_template('servicos.html', servicos=servicos)

@app.route('/servicos/add', methods=['POST'])
def add_servico():
    nome = request.form.get('nome')
    duracao = request.form.get('duracao') or 60
    try:
        duracao = int(duracao)
    except:
        duracao = 60
    if not nome:
        flash('Nome do serviço é obrigatório', 'error')
        return redirect(url_for('listar_servicos'))
    s = Servico(nome=nome, duracao=duracao)
    db.session.add(s)
    db.session.commit()
    flash('Serviço adicionado', 'success')
    return redirect(url_for('listar_servicos'))

@app.route('/servicos/delete/<int:id>')
def delete_servico(id):
    s = Servico.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    flash('Serviço removido', 'success')
    return redirect(url_for('listar_servicos'))


@app.route('/agendamentos')
def listar_agendamentos():
    agendamentos = Agendamento.query.join(Cliente).join(Servico).order_by(Agendamento.inicio).all()
    clientes = Cliente.query.order_by(Cliente.nome).all()
    servicos = Servico.query.order_by(Servico.nome).all()
    return render_template('agendamentos.html', agendamentos=agendamentos, clientes=clientes, servicos=servicos)

def conflito_exists(servico_id, inicio, duracao):
    fim = inicio + timedelta(minutes=duracao)
    ags = Agendamento.query.filter_by(servico_id=servico_id).all()
    for a in ags:
        a_inicio = a.inicio
        a_fim = a_inicio + timedelta(minutes=a.servico.duracao)
        if (inicio < a_fim) and (a_inicio < fim):
            return True
    return False

@app.route('/agendamentos/add', methods=['POST'])
def add_agendamento():
    cliente_id = request.form.get('cliente_id')
    servico_id = request.form.get('servico_id')
    data = request.form.get('data')  
    hora = request.form.get('hora') 
    if not (cliente_id and servico_id and data and hora):
        flash('Todos os campos são obrigatórios', 'error')
        return redirect(url_for('listar_agendamentos'))
    try:
        inicio = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")
    except ValueError:
        flash('Data/hora inválida', 'error')
        return redirect(url_for('listar_agendamentos'))
    servico = Servico.query.get(int(servico_id))
    if not servico:
        flash('Serviço inválido', 'error')
        return redirect(url_for('listar_agendamentos'))
    if conflito_exists(servico.id, inicio, servico.duracao):
        flash('Conflito de horário: já existe agendamento para esse serviço nesse horário', 'error')
        return redirect(url_for('listar_agendamentos'))
    a = Agendamento(cliente_id=int(cliente_id), servico_id=int(servico_id), inicio=inicio)
    db.session.add(a)
    db.session.commit()
    flash('Agendamento criado', 'success')
    return redirect(url_for('listar_agendamentos'))

@app.route('/agendamentos/delete/<int:id>')
def delete_agendamento(id):
    a = Agendamento.query.get_or_404(id)
    db.session.delete(a)
    db.session.commit()
    flash('Agendamento removido', 'success')
    return redirect(url_for('listar_agendamentos'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
