import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

def run_linear_regression():
    cunningham = pd.read_csv('data/exported/cunningham_games_table_all_seasons.csv')
    ivey = pd.read_csv('data/exported/ivey_games_table_all_seasons.csv')
    duren = pd.read_csv('data/exported/duren_games_table_all_seasons.csv')

    def split_data(player_data, target):
        X = player_data[['MIN', 'FGA', 'TOV']]
        y = player_data[target]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(X_train, y_train):
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model

    def calculate_probabilities(predictions, actual):
        mean = np.mean(actual)
        median = np.median(actual)
        mode = actual.mode()[0]
        maximum = np.max(actual)
        minimum = np.min(actual)

        probabilities = {
            'above_mean': np.mean(predictions > mean),
            'below_mean': np.mean(predictions < mean),
            'above_median': np.mean(predictions > median),
            'below_median': np.mean(predictions < median),
            'above_mode': np.mean(predictions > mode),
            'below_mode': np.mean(predictions < mode),
            'above_maximum': np.mean(predictions > maximum),
            'below_maximum': np.mean(predictions < maximum),
            'above_minimum': np.mean(predictions > minimum),
            'below_minimum': np.mean(predictions < minimum)
        }

        return probabilities

    def plot_probabilities(probabilities, title, filename):
        categories = list(probabilities.keys())
        values = list(probabilities.values())

        fig = go.Figure(data=[
            go.Bar(name='Probability', x=categories, y=values)
        ])

        fig.update_layout(
            title=title,
            xaxis_title='Category',
            yaxis_title='Probability',
            barmode='group'
        )

        fig.write_html(filename)

    def process_player_data(player_data, player_name):
        targets = ['PTS', 'AST', 'REB']
        for target in targets:
            X_train, X_test, y_train, y_test = split_data(player_data, target)
            model = train_model(X_train, y_train)
            predictions = model.predict(X_test)
            probabilities = calculate_probabilities(predictions, y_test)
            plot_probabilities(probabilities, f'{player_name} {target} Probabilities', f'dashboards/bar/{player_name}_{target.lower()}_probabilities.html')

    # Processar dados de todos os jogadores
    process_player_data(cunningham, 'Cunningham')
    process_player_data(ivey, 'Ivey')
    process_player_data(duren, 'Duren')

