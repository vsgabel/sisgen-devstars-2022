from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_SERVER"] = 'smtp.mailtrap.io'
app.config["MAIL_PORT"] = "587" 
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "3237568cc08f00"
app.config["MAIL_PASSWORD"] = "959d477fc33a0a"

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/contato", methods=['GET', 'POST'])
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

if __name__ == "__main__":
    app.run(debug=True)