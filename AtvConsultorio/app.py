from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    dados_especialidades = {
        "Cardiologia": [
            {
                "nome": "Dr. André Souza",
                "crm": "CRM/MG 18432",
                "planos": ["Unimed", "Amil", "SulAmérica"],
            },
            {
                "nome": "Dra. Fernanda Melo",
                "crm": "CRM/MG 22105",
                "planos": ["Bradesco Saúde", "Unimed"],
            },
        ],
        "Pediatria": [
            {
                "nome": "Dra. Carla Nunes",
                "crm": "CRM/MG 15780",
                "planos": ["Unimed", "Hapvida", "Amil"],
            },
            {
                "nome": "Dr. Lucas Ribeiro",
                "crm": "CRM/MG 31209",
                "planos": ["SulAmérica", "NotreDame"],
            },
        ],
        "Dermatologia": [
            {
                "nome": "Dra. Juliana Costa",
                "crm": "CRM/MG 29801",
                "planos": ["Amil", "Bradesco Saúde"],
            },
        ],
    }

    especialidade = request.form.get("especialidade")
    medicos = dados_especialidades.get(especialidade)
    
    print(medicos)

    if request.method == "POST":
        return render_template(
            "painel.html", especialidade=especialidade, medicos=medicos
        )

    return render_template("painel.html")


if __name__ == "__main__":
    app.run(debug=True)
