from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que outros serviços acessem a API
producao_dados = []

@app.route('/')
def index():
    return render_template('index.html', dados=producao_dados)

@app.route('/registrar', methods=['POST'])
def registrar():
    etapa = request.form.get('etapa')
    status = request.form.get('status')
    if etapa and status:
        producao_dados.append({'etapa': etapa, 'status': status})
        return jsonify({'mensagem': 'Registro salvo com sucesso!', 'dados': producao_dados})
    return jsonify({'erro': 'Dados inválidos'}), 400

@app.route('/api/producao', methods=['GET'])
def api_producao():
    return jsonify(producao_dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
