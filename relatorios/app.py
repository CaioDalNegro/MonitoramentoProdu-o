from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def relatorios():
    # URLs dos outros serviços (exemplo)
    url_producao = "http://localhost:5001/api/producao"
    url_pecas = "http://localhost:5002/api/pecas"
    url_qualidade = "http://localhost:5003/api/qualidade"

    try:
        resp_producao = requests.get(url_producao)
        dados_producao = resp_producao.json() if resp_producao.status_code == 200 else {}

        resp_pecas = requests.get(url_pecas)
        dados_pecas = resp_pecas.json() if resp_pecas.status_code == 200 else {}

        resp_qualidade = requests.get(url_qualidade)
        dados_qualidade = resp_qualidade.json() if resp_qualidade.status_code == 200 else {}

    except Exception as e:
        # Em caso de erro, pode logar e setar dados vazios
        dados_producao = {}
        dados_pecas = {}
        dados_qualidade = {}

    # Aqui você consolida os dados para o template
    # Por exemplo:
    dias = dados_producao.get('dias', ["Seg", "Ter", "Qua", "Qui", "Sex"])
    producao_diaria = dados_producao.get('producao_diaria', [10, 20, 15, 12, 18])

    nomes_veiculos = [peca['veiculo'] for peca in dados_pecas]
    contagem_pecas = {}
    for v in nomes_veiculos:
        contagem_pecas[v] = contagem_pecas.get(v, 0) + 1

    nomes_veiculos = list(contagem_pecas.keys())
    contagem_pecas = list(contagem_pecas.values())

    # Você pode também incluir dados da qualidade, conforme seu modelo

    return render_template("relatorios.html",
                           dias=dias,
                           producao_diaria=producao_diaria,
                           nomes_veiculos=nomes_veiculos,
                           contagem_pecas=contagem_pecas,
                           dados_qualidade=dados_qualidade)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
