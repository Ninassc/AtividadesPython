from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

pasta = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta, "database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    telefone = db.Column(db.String(20), nullable = False)

with app.app_context():
    db.create_all()

@app.route('/')
def lista():
    alunos = Aluno.query.order_by(Aluno.id.desc()).all()
    total_alunos = Aluno.query.count()

    return render_template(
        'lista.html',
        alunos = alunos,
        total_alunos = total_alunos
    )

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]

        aluno = Aluno(
            nome = nome,
            telefone = telefone
        )

        db.session.add(aluno)
        db.session.commit()

        return redirect('/')
    
    return render_template('formulario.html')

if __name__ == "__main__":
    app.run(debug=True)