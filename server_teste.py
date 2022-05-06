from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>oi</h1>"

@app.route("/nome/<nome>")
@app.route("/nome")
def nome(nome=None):
    if nome:
        return f"<h1>Bem-vindo, {nome}</h1>"
    return "<h1>Seja bem-vindo</h1>"

@app.route("/numero/<int:num>")
def numero(num):
    return f"O número é {num}"

@app.route("/cliente/<int:idade>")
@app.route("/cliente/<nome>")
@app.route("/cliente/<int:idade>/<nome>")
def nao_numero(idade=None, nome=None):
    return f"Você digitou o texto {idade}"

@app.route("/teste", methods=['GET', 'POST'])
def teste():
    data = request.form or {}

    if data:
        link = "http:\\\\" + data['link']
        return redirect(link)

    string = \
    f"""
    <html>
        <body>
            <form method="post">
                <input type="text" name="link">
                <input type="submit">
            </form>
        </body>
    </html>
    """

    return string

@app.route("/teste2")
def teste2():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)