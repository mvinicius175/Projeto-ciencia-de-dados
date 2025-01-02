import numpy as np
import pandas as pd
from scipy.stats import gumbel_r
import matplotlib.pyplot as plt
import plotly.graph_objects as go

cunningham = pd.read_csv('data/exported/cunningham_games_table_all_seasons.csv')
ivey       = pd.read_csv('data/exported/ivey_games_table_all_seasons.csv')
duren      = pd.read_csv('data/exported/duren_games_table_all_seasons.csv')

def fit_gumbel(data):
    params = gumbel_r.fit(data)
    return params

def probability_above_x(params, x):
    return 1 - gumbel_r.cdf(x, *params)

def probability_at_least_x(params, x):
    return 1 - gumbel_r.cdf(x, *params)

def probability_at_most_x(params, x):
    return gumbel_r.cdf(x, *params)

def proportion_below_or_equal_x(data, x):
    return np.mean(data <= x)

def values_below_x(data, x):
    return data[data < x]

def proportion_below_x(data, x):
    return np.mean(data < x)

cunningham_points = cunningham['PTS']
cunningham_rebounds = cunningham['REB']
cunningham_assists = cunningham['AST']
cunningham_points_params = fit_gumbel(cunningham_points)
cunningham_rebounds_params = fit_gumbel(cunningham_rebounds)
cunningham_assists_params = fit_gumbel(cunningham_assists)

ivey_points = ivey['PTS']
ivey_rebounds = ivey['REB']
ivey_assists = ivey['AST']
ivey_points_params = fit_gumbel(ivey_points)
ivey_rebounds_params = fit_gumbel(ivey_rebounds)
ivey_assists_params = fit_gumbel(ivey_assists)

duren_points = duren['PTS']
duren_rebounds = duren['REB']
duren_assists = duren['AST']
duren_points_params = fit_gumbel(duren_points)
duren_rebounds_params = fit_gumbel(duren_rebounds)
duren_assists_params = fit_gumbel(duren_assists)

x = 30  # Points threshold
y = 20  # Rebounds threshold
z = 10  # Assists threshold


def plot_probabilities_and_proportions(data, params, title, x_label, file_name):
    x_values = np.linspace(min(data), max(data), 100)
    prob_above = [probability_above_x(params, x) for x in x_values]
    prob_at_least = [probability_at_least_x(params, x) for x in x_values]
    prob_at_most = [probability_at_most_x(params, x) for x in x_values]
    prop_below_or_equal = [proportion_below_or_equal_x(data, x) for x in x_values]
    prop_below = [proportion_below_x(data, x) for x in x_values]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=prob_above, mode='lines', name='Probabilidade de mais que x'))
    fig.add_trace(go.Scatter(x=x_values, y=prob_at_least, mode='lines', name='Probabilidade de pelo menos x'))
    fig.add_trace(go.Scatter(x=x_values, y=prob_at_most, mode='lines', name='Probabilidade de no máximo x'))
    fig.add_trace(go.Scatter(x=x_values, y=prop_below_or_equal, mode='lines', name='Proporção de valores menores ou iguais a x'))
    fig.add_trace(go.Scatter(x=x_values, y=prop_below, mode='lines', name='Proporção de valores abaixo de x'))

    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title='Probabilidade/Proporção',
        legend_title='Legenda',
        template='plotly_white'
    )

    fig.write_html(file_name)

# Cunningham
plot_probabilities_and_proportions(cunningham_points, cunningham_points_params, 'Probabilidades e Proporções para Pontos de Cunningham', 'Pontos', 'dashboards/line/cunningham_points_probabilities.html')
plot_probabilities_and_proportions(cunningham_rebounds, cunningham_rebounds_params, 'Probabilidades e Proporções para Rebotes de Cunningham', 'Rebotes', 'dashboards/line/cunningham_rebounds_probabilities.html')
plot_probabilities_and_proportions(cunningham_assists, cunningham_assists_params, 'Probabilidades e Proporções para Assistências de Cunningham', 'Assistências', 'dashboards/line/cunningham_assists_probabilities.html')

# Ivey
plot_probabilities_and_proportions(ivey_points, ivey_points_params, 'Probabilidades e Proporções para Pontos de Ivey', 'Pontos', 'dashboards/line/ivey_points_probabilities.html')
plot_probabilities_and_proportions(ivey_rebounds, ivey_rebounds_params, 'Probabilidades e Proporções para Rebotes de Ivey', 'Rebotes', 'dashboards/line/ivey_rebounds_probabilities.html')
plot_probabilities_and_proportions(ivey_assists, ivey_assists_params, 'Probabilidades e Proporções para Assistências de Ivey', 'Assistências', 'dashboards/line/ivey_assists_probabilities.html')

# Duren
plot_probabilities_and_proportions(duren_points, duren_points_params, 'Probabilidades e Proporções para Pontos de Duren', 'Pontos', 'dashboards/line/duren_points_probabilities.html')
plot_probabilities_and_proportions(duren_rebounds, duren_rebounds_params, 'Probabilidades e Proporções para Rebotes de Duren', 'Rebotes', 'dashboards/line/duren_rebounds_probabilities.html')
plot_probabilities_and_proportions(duren_assists, duren_assists_params, 'Probabilidades e Proporções para Assistências de Duren', 'Assistências', 'dashboards/line/duren_assists_probabilities.html')
