from app.main import main
from app import mail
from flask import render_template, request
from flask_mail import Message

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/registro")
def registro():
    return render_template("registro.html")

@main.route("/contato", methods=['GET', 'POST'])
def contato():
    dados = request.form
    if dados:
        msg = Message("Contato", sender="Sistema Genérico 1.0", recipients=["victor.gabel@gmail.com", dados['email']])
        # msg.body = f"""
        # Formulário de contato preenchido

        # Nome: {dados['nome']}
        # E-mail: {dados['email']}
        # Mensagem:
        # {dados['mensagem']}

        # ------
        # Esta é uma mensagem automática. Favor não responder.
        # """
        msg.html = render_template('email/contato.html', nome=dados['nome'], email=dados['email'],
                                   mensagem=dados['mensagem'])

        mail.send(msg)
    return render_template("contato.html")