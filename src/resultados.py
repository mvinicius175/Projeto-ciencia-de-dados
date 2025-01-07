from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    #########################################################################################################
    # Parte 1

    # RF 1
    west_conference = pd.read_csv('data/processed/west_conference.csv')
    east_conference = pd.read_csv('data/processed/east_conference.csv')
    # RF 3
    pistons_summary_23_24 = pd.read_csv('data/exported/pistons_summary_23_24.csv')
    pistons_summary_24_25 = pd.read_csv('data/exported/pistons_summary_24_25.csv')
    # RF 4
    pistons_summary_23_24_pt1 = pd.read_csv('data/exported/pistons_summary_23_24_pt1_.csv')
    pistons_summary_24_25_pt1 = pd.read_csv('data/exported/pistons_summary_24_25_pt1_.csv')
    # RF 5
    pistons_summary_23_24_pt2 = pd.read_csv('data/exported/pistons_summary_23_24_pt2_.csv')
    pistons_summary_24_25_pt2 = pd.read_csv('data/exported/pistons_summary_24_25_pt2_.csv')
    # RF 6
    pistons_defensive_summary_23_24 = pd.read_csv('data/exported/pistons_defensive_summary_23_24.csv')
    pistons_defensive_summary_24_25 = pd.read_csv('data/exported/pistons_defensive_summary_24_25.csv')
    # RF 7
    pistons_games_table = pd.concat([pd.read_csv('data/exported/pistons_games_table_23_24.csv'), pd.read_csv('data/exported/pistons_games_table_24_25.csv')], ignore_index=True)
    # RF 8
    with open('dashboards/bar/pistons_home_away_wins_losses_23_24.html', 'r') as f:
        pistons_win_losses_23_24 = f.read()
    with open('dashboards/bar/pistons_home_away_wins_losses_24_25.html', 'r') as f:
        pistons_win_losses_24_25 = f.read()
    with open('dashboards/bar/pistons_home_away_wins_losses_all.html', 'r') as f:
        pistons_win_losses_both_seasons = f.read()
    with open('dashboards/histogram/resultados_por_mês.html', 'r') as f:
        pistons_histogram = f.read()





    return f"""
    <html>
        <head>
            <title>Resultados</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h1>Resultados do Projeto</h1>
                <h2>Tabela</h2>
                {'tabela_html'}
                <h2>Gráfico</h2>
                <img src="data:image/png;base64,{'plot_url'}" />
            </div>
        </body>
    </html>
"""
