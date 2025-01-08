import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from pygam import PoissonGAM, s
from scipy.stats import poisson
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_predictions(home_or_away):
    cunningham = pd.read_csv('data/exported/cunningham_games_table_all_seasons.csv')
    ivey = pd.read_csv('data/exported/ivey_games_table_all_seasons.csv')
    duren = pd.read_csv('data/exported/duren_games_table_all_seasons.csv')

    cunningham['Home or Road'] = cunningham['Home or Road'].map({'Home': 0, 'Road': 1})
    ivey['Home or Road'] = ivey['Home or Road'].map({'Home': 0, 'Road': 1})
    duren['Home or Road'] = duren['Home or Road'].map({'Home': 0, 'Road': 1})

    def train_and_predict(player_data, home_away):
        # Selecionar features e alvos
        features = ['Home or Road', 'MIN', 'FGA']
        X = player_data[features]
        y_points = player_data['PTS']
        y_rebounds = player_data['REB']
        y_assists = player_data['AST']

        # Divisão em treino e teste
        X_train, X_test, y_train_points, y_test_points = train_test_split(X, y_points, test_size=0.2, random_state=42)
        _, _, y_train_rebounds, y_test_rebounds = train_test_split(X, y_rebounds, test_size=0.2, random_state=42)
        _, _, y_train_assists, y_test_assists = train_test_split(X, y_assists, test_size=0.2, random_state=42)

        # Treinamento dos modelos
        gam_points = PoissonGAM(s(0) + s(1) + s(2)).fit(X_train, y_train_points)
        gam_rebounds = PoissonGAM(s(0) + s(1) + s(2)).fit(X_train, y_train_rebounds)
        gam_assists = PoissonGAM(s(0) + s(1) + s(2)).fit(X_train, y_train_assists)

        # Previsões para o próximo jogo
        X_value = [[home_away, player_data['MIN'].mean(), player_data['FGA'].mean()]]
        mu_points = gam_points.predict_mu(X_value)
        mu_rebounds = gam_rebounds.predict_mu(X_value)
        mu_assists = gam_assists.predict_mu(X_value)

        # Definir thresholds como a média dos pontos, rebotes e assistências
        threshold_points = y_points.mean()
        threshold_rebounds = y_rebounds.mean()
        threshold_assists = y_assists.mean()

        # Probabilidades de valores extremos
        prob_above_threshold_points = 1 - poisson.cdf(threshold_points, mu_points)
        prob_below_threshold_points = poisson.cdf(threshold_points, mu_points)
        prob_above_threshold_rebounds = 1 - poisson.cdf(threshold_rebounds, mu_rebounds)
        prob_below_threshold_rebounds = poisson.cdf(threshold_rebounds, mu_rebounds)
        prob_above_threshold_assists = 1 - poisson.cdf(threshold_assists, mu_assists)
        prob_below_threshold_assists = poisson.cdf(threshold_assists, mu_assists)

        return {
            'points': (mu_points, prob_above_threshold_points, prob_below_threshold_points),
            'rebounds': (mu_rebounds, prob_above_threshold_rebounds, prob_below_threshold_rebounds),
            'assists': (mu_assists, prob_above_threshold_assists, prob_below_threshold_assists)
        }, gam_points, gam_rebounds, gam_assists

    def visualize(gam_points, gam_rebounds, gam_assists, X, y_points, y_rebounds, y_assists, output_png='visualizations.png'):
        # Configurar gráficos interativos com plotly
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=[
                "Points: Coefficients", "Points: Predictions vs Actual",
                "Rebounds: Coefficients", "Rebounds: Predictions vs Actual",
                "Assists: Coefficients", "Assists: Predictions vs Actual"
            ]
        )

        titles = ['Points', 'Rebounds', 'Assists']
        models = [gam_points, gam_rebounds, gam_assists]
        y_values = [y_points, y_rebounds, y_assists]

        for i, (model, y, title) in enumerate(zip(models, y_values, titles)):
            row = i + 1

            # Gráfico de Coeficientes
            fig.add_trace(
                go.Scatter(y=model.coef_, mode='lines+markers', name=f'{title}: Coefficients'),
                row=row, col=1
            )

            # Gerar X_pred com o mesmo número de features
            X_pred = np.tile(X.mean(axis=0), (100, 1))  # Média dos valores em X para preencher
            X_pred[:, 1] = np.linspace(X['MIN'].min(), X['MIN'].max(), 100)  # Variar minutos jogados

            # Previsões
            y_pred = model.predict(X_pred)
            fig.add_trace(
                go.Scatter(x=X_pred[:, 1], y=y_pred, mode='lines', name=f'{title}: Predicted'),
                row=row, col=2
            )
            fig.add_trace(
                go.Scatter(x=X['MIN'], y=y, mode='markers', name=f'{title}: Actual', marker=dict(color='red')),
                row=row, col=2
            )

        # Atualizar layout
        fig.update_layout(
            height=900, width=1200,
            title_text="Visualizations",
            showlegend=False
        )

        # Salvar em arquivo PNG
        fig.write_image(output_png)

    predictions, gam_points, gam_rebounds, gam_assists = train_and_predict(cunningham, home_or_away)

    # Criar DataFrame com as previsões
    predictions_df = pd.DataFrame({
        'Player': ['Cunningham'],
        'Points': [predictions['points'][0][0]],
        'Prob_Points_Above_Average': [predictions['points'][1][0]],
        'Prob_Points_Below_Average': [predictions['points'][2][0]],
        'Assists': [predictions['assists'][0][0]],
        'Prob_Assists_Above_Average': [predictions['assists'][1][0]],
        'Prob_Assists_Below_Average': [predictions['assists'][2][0]],
        'Rebounds': [predictions['rebounds'][0][0]],
        'Prob_Rebounds_Above_Average': [predictions['rebounds'][1][0]],
        'Prob_Rebounds_Below_Average': [predictions['rebounds'][2][0]]
    })

    # Salvar DataFrame em um arquivo CSV
    predictions_df.to_csv('data/exported/cunningham_predictions.csv', index=False)

    # Cunningham
    X_cunningham = cunningham[['Home or Road', 'MIN', 'FGA']]
    y_cunningham_points = cunningham['PTS']
    y_cunningham_rebounds = cunningham['REB']
    y_cunningham_assists = cunningham['AST']
    visualize(gam_points, gam_rebounds, gam_assists, X_cunningham, y_cunningham_points, y_cunningham_rebounds, y_cunningham_assists, 'static/dashboards/predictions/cunningham_predictions.png')

    # Ivey
    predictions_ivey, gam_points_ivey, gam_rebounds_ivey, gam_assists_ivey = train_and_predict(ivey, home_or_away)
    # Criar DataFrame com as previsões de Ivey
    predictions_ivey_df = pd.DataFrame({
        'Player': ['Ivey'],
        'Points': [predictions_ivey['points'][0][0]],
        'Prob_Points_Above_Average': [predictions_ivey['points'][1][0]],
        'Prob_Points_Below_Average': [predictions_ivey['points'][2][0]],
        'Assists': [predictions_ivey['assists'][0][0]],
        'Prob_Assists_Above_Average': [predictions_ivey['assists'][1][0]],
        'Prob_Assists_Below_Average': [predictions_ivey['assists'][2][0]],
        'Rebounds': [predictions_ivey['rebounds'][0][0]],
        'Prob_Rebounds_Above_Average': [predictions_ivey['rebounds'][1][0]],
        'Prob_Rebounds_Below_Average': [predictions_ivey['rebounds'][2][0]]
    })

    # Salvar DataFrame em um arquivo CSV
    predictions_ivey_df.to_csv('data/exported/ivey_predictions.csv', index=False)

    X_ivey = ivey[['Home or Road', 'MIN', 'FGA']]
    y_ivey_points = ivey['PTS']
    y_ivey_rebounds = ivey['REB']
    y_ivey_assists = ivey['AST']
    visualize(gam_points_ivey, gam_rebounds_ivey, gam_assists_ivey, X_ivey, y_ivey_points, y_ivey_rebounds, y_ivey_assists, 'static/dashboards/predictions/ivey_predictions.png')

    # Duren
    predictions_duren, gam_points_duren, gam_rebounds_duren, gam_assists_duren = train_and_predict(duren, home_or_away)
    # Criar DataFrame com as previsões de Duren
    predictions_duren_df = pd.DataFrame({
        'Player': ['Duren'],
        'Points': [predictions_duren['points'][0][0]],
        'Prob_Points_Above_Average': [predictions_duren['points'][1][0]],
        'Prob_Points_Below_Average': [predictions_duren['points'][2][0]],
        'Assists': [predictions_duren['assists'][0][0]],
        'Prob_Assists_Above_Average': [predictions_duren['assists'][1][0]],
        'Prob_Assists_Below_Average': [predictions_duren['assists'][2][0]],
        'Rebounds': [predictions_duren['rebounds'][0][0]],
        'Prob_Rebounds_Above_Average': [predictions_duren['rebounds'][1][0]],
        'Prob_Rebounds_Below_Average': [predictions_duren['rebounds'][2][0]]
    })

    # Salvar DataFrame em um arquivo CSV
    predictions_duren_df.to_csv('data/exported/duren_predictions.csv', index=False)

    X_duren = duren[['Home or Road', 'MIN', 'FGA']]
    y_duren_points = duren['PTS']
    y_duren_rebounds = duren['REB']
    y_duren_assists = duren['AST']
    visualize(gam_points_duren, gam_rebounds_duren, gam_assists_duren, X_duren, y_duren_points, y_duren_rebounds, y_duren_assists, 'static/dashboards/predictions/duren_predictions.png')
