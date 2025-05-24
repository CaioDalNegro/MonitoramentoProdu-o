from flask import Flask, render_template

app = Flask(__name__)

@app.route("/relatorios")
def relatorios():
    dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]
    producao_diaria = [10, 20, 15, 12, 18]
    nomes_veiculos = ["Carro A", "Carro B", "Caminhão"]
    contagem_pecas = [5, 3, 2]

    return render_template("relatorios.html",
                           dias=dias,
                           producao_diaria=producao_diaria,
                           nomes_veiculos=nomes_veiculos,
                           contagem_pecas=contagem_pecas)

if __name__ == "__main__":
    app.run(debug=True)
