import pandas as pd
import plotly.express as px

pistons_23_24_summary = pd.read_csv('data/exported/pistons_23_24_summary.csv')
pistons_24_25_summary = pd.read_csv('data/exported/pistons_24_25_summary.csv')

pistons_23_24_summary['Season'] = '2023-24'
pistons_24_25_summary['Season'] = '2024-25'

pistons_both_seasons_summary = pd.concat([pistons_23_24_summary, pistons_24_25_summary], ignore_index=True)

pistons_both_seasons_summary['Vitórias'] = pistons_both_seasons_summary['Total Wins']
pistons_both_seasons_summary['Vitórias em casa'] = pistons_both_seasons_summary['Home Wins']
pistons_both_seasons_summary['Vitórias fora de casa'] = pistons_both_seasons_summary['Road Wins']
pistons_both_seasons_summary['Derrotas'] = pistons_both_seasons_summary['Total Losses']
pistons_both_seasons_summary['Derrotas em casa'] = pistons_both_seasons_summary['Home Losses']
pistons_both_seasons_summary['Derrotas fora de casa'] = pistons_both_seasons_summary['Road Losses']

pistons_home_away_win_losses_all = pistons_both_seasons_summary.melt(id_vars=['Season'], value_vars=['Vitórias em casa', 'Vitórias fora de casa', 'Derrotas em casa', 'Derrotas fora de casa'], var_name='Resultado', value_name='Quantidade')

pistons_home_away_all_data = pistons_home_away_win_losses_all.groupby(['Resultado']).sum(numeric_only=True).reset_index()

category_order = ['Vitórias em casa', 'Vitórias fora de casa', 'Derrotas em casa', 'Derrotas fora de casa']

pistons_home_away_all_data_graph = px.pie(pistons_home_away_all_data, names='Resultado', values='Quantidade', color='Resultado',
              color_discrete_map={'Vitórias em casa': 'green', 'Vitórias fora de casa': 'blue', 'Derrotas em casa':'red', 'Derrotas fora de casa': 'brown'},
              title='Vitórias e derrotas do Detroit Pistons nas temporadas 2023-24 e 2024-25',
              category_orders={'Resultado': category_order})

pistons_home_away_23_24_data = pistons_home_away_win_losses_all[pistons_home_away_win_losses_all['Season'] == '2023-24']
pistons_home_away_24_25_data = pistons_home_away_win_losses_all[pistons_home_away_win_losses_all['Season'] == '2024-25']

pistons_home_away_23_24_data_grouped = pistons_home_away_23_24_data.groupby(['Resultado']).sum(numeric_only=True).reset_index()
pistons_home_away_24_25_data_grouped = pistons_home_away_24_25_data.groupby(['Resultado']).sum(numeric_only=True).reset_index()

pistons_home_away_23_24_graph = px.pie(pistons_home_away_23_24_data_grouped, names='Resultado', values='Quantidade', color='Resultado',
              color_discrete_map={'Vitórias em casa': 'green', 'Vitórias fora de casa': 'blue', 'Derrotas em casa':'red', 'Derrotas fora de casa': 'brown'},
              title='Vitórias e derrotas do Detroit Pistons na temporada 2023-24',
              category_orders={'Resultado': category_order})

pistons_home_away_24_25_graph = px.pie(pistons_home_away_24_25_data_grouped, names='Resultado', values='Quantidade', color='Resultado',
              color_discrete_map={'Vitórias em casa': 'green', 'Vitórias fora de casa': 'blue', 'Derrotas em casa':'red', 'Derrotas fora de casa': 'brown'},
              title='Vitórias e derrotas do Detroit Pistons na temporada 2024-25',
              category_orders={'Resultado': category_order})

pistons_home_away_all_data_graph.write_html('dashboards/charts/pie/pistons_home_away_wins_losses_all.html')
pistons_home_away_23_24_graph.write_html('dashboards/charts/pie/pistons_home_away_wins_losses_23_24.html')
pistons_home_away_24_25_graph.write_html('dashboards/charts/pie/pistons_home_away_wins_losses_24_25.html')

