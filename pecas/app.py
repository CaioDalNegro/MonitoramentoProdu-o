from flask import Flask, request, jsonify, render_template
from pecas_data import listar_pecas, adicionar_peca

app = Flask(__name__)

@app.route("/")
def home():
    pecas = listar_pecas()
    return render_template("index.html", pecas=pecas)

@app.route("/api/pecas", methods=["GET"])
def api_listar_pecas():
    return jsonify(listar_pecas())

@app.route("/api/pecas", methods=["POST"])
def api_adicionar_peca():
    data = request.json
    nome = data.get("nome")
    veiculo = data.get("veiculo")
    if not nome or not veiculo:
        return jsonify({"erro": "Campos 'nome' e 'veiculo' são obrigatórios."}), 400
    nova_peca = adicionar_peca(nome, veiculo)
    return jsonify(nova_peca), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)