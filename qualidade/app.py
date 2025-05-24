from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
inspecoes = []

@app.route('/')
def index():
    try:
        resposta = requests.get('http://producao:5000/api/producao')  # nome do serviço no Docker Compose
        producao = resposta.json()
    except Exception:
        producao = []
    return render_template('index.html', inspecoes=inspecoes, producao=producao)

@app.route('/registrar', methods=['POST'])
def registrar():
    peca = request.form.get('peca')
    resultado = request.form.get('resultado')
    observacao = request.form.get('observacao')
    if peca and resultado:
        inspecoes.append({
            'peca': peca,
            'resultado': resultado,
            'observacao': observacao or ''
        })
        return jsonify({'mensagem': 'Inspeção registrada com sucesso!', 'dados': inspecoes})
    return jsonify({'erro': 'Dados inválidos'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
