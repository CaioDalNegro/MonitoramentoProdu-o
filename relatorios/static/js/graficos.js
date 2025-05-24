// static/js/graficos.js

window.addEventListener('DOMContentLoaded', () => {
    // Pega os elementos canvas
    const graficoProducao = document.getElementById('graficoProducao');
    const graficoPecas = document.getElementById('graficoPecas');

    // Extrai os dados dos atributos data- do HTML e transforma em arrays JS
    const dias = JSON.parse(graficoProducao.dataset.dias);
    const producaoDiaria = JSON.parse(graficoProducao.dataset.producao);

    const nomesVeiculos = JSON.parse(graficoPecas.dataset.nomes);
    const contagemPecas = JSON.parse(graficoPecas.dataset.contagem);

    // Cria o gráfico de Produção
    const ctx1 = graficoProducao.getContext('2d');
    new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: dias,
            datasets: [{
                label: 'Produção diária',
                data: producaoDiaria,
                backgroundColor: 'rgba(54, 162, 235, 0.7)'
            }]
        }
    });

    // Cria o gráfico de Peças por Veículo
    const ctx2 = graficoPecas.getContext('2d');
    new Chart(ctx2, {
        type: 'pie',
        data: {
            labels: nomesVeiculos,
            datasets: [{
                label: 'Peças por veículo',
                data: contagemPecas,
                backgroundColor: ['#007bff', '#28a745', '#ffc107', '#dc3545']
            }]
        }
    });
});
