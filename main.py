
from src.data_extraction import extract_data
from src.data_cleaning import clean_data
from src.data_analisys import analyze_data
from src.gumbel_model import run_gumbel_model
from src.linear_regression import run_linear_regression
from src.logistic_regression import run_logistic_regression
from src.predictions import make_predictions
from src.visualization.bar_charts import plot_bar_charts
from src.visualization.box_plot import plot_box_plot
from src.visualization.distribution_graph import plot_distribution_graph
from src.visualization.histograms import plot_histograms
from src.visualization.line_charts import plot_line_charts
from src.visualization.pie_charts import plot_pie_charts
from src.visualization.radar_charts import plot_radar_charts
from src.visualization.scatter_plots import plot_scatter_plots

def main():
    print("Extraindo os dados...")
    extract_data()
    print("Limpando os dados...")
    clean_data()
    print("Analisando os dados...")
    search_term = analyze_data()
    print("Criando gráficos...")
    plot_scatter_plots()
    plot_radar_charts()
    plot_pie_charts()
    plot_line_charts()
    plot_histograms()
    plot_distribution_graph()
    plot_box_plot()
    plot_bar_charts()
    print("Rodando o modelo Gumbel...")
    run_gumbel_model()
    print("Rodando a regressão linear...")
    run_linear_regression()
    print("Rodando a regressão logística...")
    run_logistic_regression()
    print("Fazendo previsões...")
    home_or_away = int(input("Digite 0 se o jogo for em casa ou digite 1 se for fora de casa: "))
    while home_or_away != 0 and home_or_away != 1:
        home_or_away = int(input("Digite 0 se o jogo for em casa ou digite 1 se for fora de casa: "))
    make_predictions(home_or_away)

if __name__ == "__main__":
    main()
