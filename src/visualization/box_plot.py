import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

cunningham_games = pd.read_csv('data/exported/cunningham_games_table_24_25.csv')
duren_games      = pd.read_csv('data/exported/duren_games_table_24_25.csv')
ivey_games       = pd.read_csv('data/exported/ivey_games_table_24_25.csv')

games = pd.concat([cunningham_games.assign(Player='Cunningham'),
                   duren_games.assign(Player='Duren'),
                   ivey_games.assign(Player='Ivey')])

games_melted = games.melt(id_vars=['Player'], value_vars=['PTS', 'REB', 'AST'],
                          var_name='Statistic', value_name='Value')

fig = px.box(games_melted, x='Statistic', y='Value', color='Player',
             points='all', title='Gráfico Box Plot para pontos, assistencias e rebotes por jogo',
             labels={'Value': 'Value', 'Statistic': 'Statistic'})

fig.write_html('dashboards/box_plot/box_plot.html')
