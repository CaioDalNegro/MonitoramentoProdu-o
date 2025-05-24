from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def relatorios():
    # Simulação dos dados de peças (substituindo a chamada ao serviço externo)
    dados_pecas = [
        {"id": 1, "nome": "Mancal", "veiculo": "HB20"},
        {"id": 2, "nome": "Filtro de óleo", "veiculo": "HB20"},
        {"id": 3, "nome": "Filtro de ar", "veiculo": "Onix"},
        {"id": 4, "nome": "Pastilha", "veiculo": "Onix"},
        {"id": 5, "nome": "Parachoque", "veiculo": "Fiesta"},
        {"id": 6, "nome": "Farol", "veiculo": "HB20"},
    ]

    # Simulação dos dados de produção
    dados_producao = {
        "dias": ["Seg", "Ter", "Qua", "Qui", "Sex"],
        "producao_diaria": [10, 20, 15, 12, 18]
    }

    # Simulação dos dados de qualidade vazia só pra não quebrar
    dados_qualidade = {}

    # Contagem das peças por veículo
    contagem_pecas_dict = {}
    for peca in dados_pecas:
        veiculo = peca.get('veiculo')
        if veiculo:
            contagem_pecas_dict[veiculo] = contagem_pecas_dict.get(veiculo, 0) + 1

    nomes_veiculos = list(contagem_pecas_dict.keys())
    contagem_pecas = list(contagem_pecas_dict.values())

    return render_template("relatorios.html",
                           dias=dados_producao['dias'],
                           producao_diaria=dados_producao['producao_diaria'],
                           nomes_veiculos=nomes_veiculos,
                           contagem_pecas=contagem_pecas,
                           dados_qualidade=dados_qualidade)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
