from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# templates

# criar a 1a. pagina do site
# toda página sempre tem:
# route
# função
# templates

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    # return nome_usuario
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
# o 'debug=True' permite hotdeploy, ou seja, a alteracao é visível sem precisar reiniciar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

