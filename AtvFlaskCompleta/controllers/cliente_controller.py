from flask import Blueprint, redirect, render_template, request, url_for

from models import Cliente

cliente_bp = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente_bp.route('/')
def index_cliente():
    clientes = Cliente.listar_clientes()
    return render_template('clientes.html', clientes=clientes)

@cliente_bp.route('/novo', methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        pontos_fidelidade = request.form.get("pontos_fidelidade")

        cliente = Cliente(
            nome = nome,
            telefone = telefone,
            pontos_fidelidade = int(pontos_fidelidade)
        )

        Cliente.salvar(cliente)

        return redirect(url_for("cliente.index_cliente"))
    
    return render_template('cadastro_cliente.html')

