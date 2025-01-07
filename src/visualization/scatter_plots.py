import pandas as pd
import plotly.express as px

def plot_scatter_plots():
    pistons_game_table_23_24 = pd.read_csv('data/exported/pistons_games_table_23_24.csv')
    pistons_game_table_24_25 = pd.read_csv('data/exported/pistons_games_table_24_25.csv')

    pistons_game_table_23_24['Season'] = '2023-24'
    pistons_game_table_24_25['Season'] = '2024-25'

    pistons_game_table_both_seasons = pd.concat([pistons_game_table_23_24, pistons_game_table_24_25], ignore_index=True)

    pistons_game_table_both_seasons['Points_Marked'], pistons_game_table_both_seasons['Points_Conceded'] = zip(
        *pistons_game_table_both_seasons['Score'].str.split(' - ').apply(lambda x: (int(x[0]), int(x[1])))
    )

    pistons_summary = pistons_game_table_both_seasons.groupby(['Season', 'Adversary']).agg({
        'Points_Marked': 'mean',
        'Points_Conceded': 'mean'
    }).reset_index()

    pistons_summary_combined = pistons_summary.groupby('Adversary').agg({
        'Points_Marked': 'mean',
        'Points_Conceded': 'mean'
    }).reset_index()

    graph_23_24 = px.scatter(
        pistons_summary[pistons_summary['Season'] == '2023-24'],
        x='Points_Conceded',
        y='Points_Marked',
        text='Adversary',
        title='Pontos Marcados vs. Sofridos - Temporada 2023-24',
        labels={'Points_Conceded': 'Pontos Sofridos (Média)', 'Points_Marked': 'Pontos Marcados (Média)'},
        color_discrete_sequence=['blue']
    )
    graph_23_24.update_traces(textposition='top center')

    graph_24_25 = px.scatter(
        pistons_summary[pistons_summary['Season'] == '2024-25'],
        x='Points_Conceded',
        y='Points_Marked',
        text='Adversary',
        title='Pontos Marcados vs. Sofridos - Temporada 2024-25',
        labels={'Points_Conceded': 'Pontos Sofridos (Média)', 'Points_Marked': 'Pontos Marcados (Média)'},
        color_discrete_sequence=['green']
    )
    graph_24_25.update_traces(textposition='top center')

    combined_graph = px.scatter(
        pistons_summary_combined,
        x='Points_Conceded',
        y='Points_Marked',
        text='Adversary',
        title='Pontos Marcados vs. Sofridos - Média das Temporadas 2023-24 e 2024-25',
        labels={'Points_Conceded': 'Pontos Sofridos (Média)', 'Points_Marked': 'Pontos Marcados (Média)'},
        color_discrete_sequence=['purple']
    )
    combined_graph.update_traces(textposition='top center')

    graph_23_24.write_image('static/dashboards/scatter/pistons_points_23_24.png')
    graph_24_25.write_image('static/dashboards/scatter/pistons_points_24_25.png')
    combined_graph.write_image('static/dashboards/scatter/pistons_points_combined.png')
