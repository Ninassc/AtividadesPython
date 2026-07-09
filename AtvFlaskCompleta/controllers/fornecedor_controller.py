from flask import Blueprint, redirect, render_template, request, url_for

from models import Fornecedor

fornecedor_bp = Blueprint('fornecedor', __name__, url_prefix='/fornecedor')

@fornecedor_bp.route('/')
def index_fornecedor():
    fornecedores = Fornecedor.listar_fornecedores()
    return render_template('fornecedores.html', fornecedores = fornecedores)

@fornecedor_bp.route('/novo', methods=["GET", "POST"])
def cadastrar_fornecedor():
    if request.method == "POST":
        nome_empresa = request.form.get("nome_empresa")
        cnpj = request.form.get("cnpj")
        produto_fornecido = request.form.get("produto_fornecido")

        fornecedor = Fornecedor(
            nome_empresa = nome_empresa,
            cnpj = cnpj,
            produto_fornecido = produto_fornecido
        )

        Fornecedor.salvar(fornecedor)

        return redirect(url_for("fornecedor.index_fornecedor"))
    
    return render_template('cadastro_fornecedor.html')


