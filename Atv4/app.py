from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gatos")
def gatos():
    return render_template('gatos.html')

@app.route("/cachorros")
def cachorros():
    return render_template('cachorros.html')

@app.route("/oncas")
def oncas():
    return render_template('oncas.html')


if __name__ == "__main__":
    app.run(debug=True)