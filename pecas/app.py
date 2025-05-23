from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#Array para armazenar em memoria
pecas = []

@app.route("/")
def home():
    return render_template("index.html", pecas=pecas)

@app.route("/api/pecas", methods=["GET"])
def listar_pecas():
    return jsonify(pecas)

@app.route("/api/pecas", methods=["POST"])
def adicionar_peca():
    data = request.json
    nova_peca = {
        "id": len(pecas) + 1,
        "nome": data["nome"],
        "veiculo": data["veiculo"]
    }
    pecas.append(nova_peca)
    return jsonify(nova_peca), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
