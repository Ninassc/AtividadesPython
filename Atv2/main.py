from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
 return """
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CURRÍCULO</title>
</head>

<body>
    <header>
        <h1>Nina Sepúlveda</h1>
    </header>
    <div class="infos">
        <h2>Informações</h2>
        <p>Idade: 17</p>
        <p>Telefone : (31) 9 7148-3681</p>
    </div>
    <div class="sobre">
        <p>
            Nina Sepúlveda, desenvolvedora web e mobile com foco em criar aplicações modernas, funcionais e
            fáceis de usar. Trabalho principalmente com React, React Native e TypeScript, desenvolvendo interfaces
            eficientes e integradas a APIs e serviços em nuvem.

            Tenho experiência na criação e consumo de APIs, uso de bancos de dados relacionais e não relacionais, e
            integração com plataformas como Supabase e Firebase. Também atuo com backend em Node.js, sempre buscando
            soluções simples, organizadas e escaláveis.

            Além do código, valorizo usabilidade e experiência do usuário, utilizando o design como parte do
            processo para entregar produtos claros, práticos e bem estruturados.
        </p>
    </div>
    <div class="hard-skills">
        <h2>HARD SKILLS</h2>
        <div class="hard-content">
            <div class="hskill" id="csharp">C#</div>
            <div class="hskill" id="aspnet">Asp.Net</div>
            <div class="hskill" id="unity">Unity</div>
            <div class="hskill" id="python">Python</div>
            <div class="hskill" id="django">Django</div>
            <div class="hskill" id="sqlserver">SQL Server</div>
            <div class="hskill" id="mysql">MySql</div>
            <div class="hskill" id="javascript">JavaScript</div>
            <div class="hskill" id="react">React</div>
            <div class="hskill" id="html5">HTML5</div>
            <div class="hskill" id="css3">CSS3</div>
            <div class="hskill" id="git">Git</div>
        </div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(debug=True)