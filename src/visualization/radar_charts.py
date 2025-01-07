import pandas as pd
import plotly.express as px

def plot_radar_charts():
    pistons_23_24_games_table = pd.read_csv('data/exported/pistons_games_table_23_24.csv')
    pistons_24_25_games_table = pd.read_csv('data/exported/pistons_games_table_24_25.csv')

    pistons_23_24_games_table['Season'] = '2023-24'
    pistons_24_25_games_table['Season'] = '2024-25'

    pistons_both_seasons_games_table = pd.concat([pistons_23_24_games_table, pistons_24_25_games_table], ignore_index=True)

    pistons_both_seasons_games_table[['Team_Points', 'Opponent_Points']] = pistons_both_seasons_games_table['Score'].str.split(' - ', expand=True).astype(int)
    pistons_both_seasons_games_table = pistons_both_seasons_games_table.rename(columns={'Home or Road': 'Casa ou Fora'})

    radar_data = (
        pistons_both_seasons_games_table.groupby(['Season', 'Casa ou Fora'])
        .agg({'Team_Points': 'mean', 'Opponent_Points': 'mean'})
        .reset_index()
        .rename(columns={'Team_Points': 'Pontos marcados', 'Opponent_Points': 'Pontos sofridos'})
    )

    combined_data = (
        pistons_both_seasons_games_table.groupby('Casa ou Fora')
        .agg({'Team_Points': 'mean', 'Opponent_Points': 'mean'})
        .reset_index()
        .rename(columns={'Team_Points': 'Pontos marcados', 'Opponent_Points': 'Pontos sofridos'})
    )

    combined_data['Season'] = 'Combined'

    radar_data = pd.concat([radar_data, combined_data], ignore_index=True)

    # Adicionando deslocamento para evitar sobreposição
    radar_data['Pontos marcados'] += 0.5
    radar_data['Pontos sofridos'] -= 0.5

    def create_radar_chart(data, season):
        season_data = data[data['Season'] == season]
        fig = px.line_polar(
            season_data.melt(id_vars=['Casa ou Fora'], value_vars=['Pontos marcados', 'Pontos sofridos']),
            r='value',
            theta='variable',
            color='Casa ou Fora',
            line_close=True,
            title=f'Gráfico radar - {season}',
        )
        return fig

    radar_23_24 = create_radar_chart(radar_data, '2023-24')
    radar_24_25 = create_radar_chart(radar_data, '2024-25')
    radar_combined = create_radar_chart(radar_data, 'Combined')

    radar_23_24.write_image('static/dashboards/radar/pistons_points_scored_23_24.png')
    radar_24_25.write_image('static/dashboards/radar/pistons_points_scored_24_25.png')
    radar_combined.write_image('static/dashboards/radar/pistons_points_scored_combined.png')
