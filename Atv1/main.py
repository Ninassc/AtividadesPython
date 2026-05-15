from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/decorator")
def index():
    return " Um decorator (decorador) em Python é uma funcionalidade poderosa e elegante que permite modificar ou estender o comportamento de funções, métodos ou classes sem alterar o seu código fonte original.Decorators são ideais para resolver problemas transversais (cross-cutting concerns) — lógicas que precisam ser aplicadas em múltiplos lugares, mas que não fazem parte da lógica de negócios principal da função"

if __name__ == "__main__":
    app.run(debug=True)
