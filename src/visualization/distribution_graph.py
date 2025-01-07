import pandas as pd
import plotly.express as px
import plotly.io as pio

def plot_distribution_graph():
    cunningham_games = pd.read_csv('data/exported/cunningham_games_table_24_25.csv')
    duren_games      = pd.read_csv('data/exported/duren_games_table_24_25.csv')
    ivey_games       = pd.read_csv('data/exported/ivey_games_table_24_25.csv')

    def distribution_graph(data, player_name, stat):
        if stat in data.columns:
            fig = px.histogram(data, x=stat, nbins=20, title=f'{player_name} - {stat} Distribution')
            fig.add_vline(x=data[stat].mean(), line_dash="dash", line_color="red", annotation_text="Mean")
            fig.add_vline(x=data[stat].median(), line_dash="dash", line_color="green", annotation_text="Median")
            fig.add_vline(x=data[stat].mode()[0], line_dash="dash", line_color="blue", annotation_text="Mode")
            pio.write_image(fig, f'static/dashboards/distribution/{player_name}_{stat}_distribution.png')
        else:
            print(f"Column '{stat}' does not exist in {player_name}'s data.")

    stats = ['PTS', 'AST', 'REB']
    players = {
        'Cunningham': cunningham_games,
        'Duren': duren_games,
        'Ivey': ivey_games
    }

    for player, data in players.items():
        for stat in stats:
            distribution_graph(data, player, stat)
