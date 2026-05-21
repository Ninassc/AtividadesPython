from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def nome():
    nome = "Nina"
    return render_template('nome.html', nome = nome)

@app.route('/nomeidade')
def nomeidade():
    nome = "Pedro"
    idade = 20
    return render_template('nome_idade.html', nome = nome, idade = idade)

@app.route('/dadousuario')
def dadosusuario():
    usuario = {"nome": "Ana", "email": "ana@email.com"}
    return render_template('dado_usuario.html', usuario = usuario)

@app.route('/listanomes')
def listanomes():
    lista_nomes = ["Samuel", "Kaique", "Isaac", "Ana", "Luana"]
    return render_template('lista_nomes.html', lista_nomes = lista_nomes)

@app.route('/notas')
def notas():
    nota = 7
    return render_template('notas.html', nota = nota)

if __name__ == "__main__":
    app.run(debug=True)