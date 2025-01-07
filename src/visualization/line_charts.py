import pandas as pd
import plotly.express as px
import plotly.io as pio


def plot_line_charts():
    pistons_23_24_summary = pd.read_csv('data/processed/detroit_pistons_games_23_24.csv')
    pistons_24_25_summary = pd.read_csv('data/processed/detroit_pistons_games_24_25.csv')

    pistons_both_seasons_summary = pd.concat([pistons_23_24_summary, pistons_24_25_summary], ignore_index=True)

    pistons_both_seasons_summary['Resultado'] = pistons_both_seasons_summary['WL'].apply(lambda x: 'Vitória' if x == 'W' else 'Derrota')

    pistons_both_seasons_summary['GAME_DATE'] = pd.to_datetime(pistons_both_seasons_summary['GAME_DATE'])

    pistons_both_seasons_summary['Ano-Mês'] = pistons_both_seasons_summary['GAME_DATE'].dt.to_period('M')

    resultados_por_mês = pistons_both_seasons_summary.groupby(['Ano-Mês', 'Resultado']).size().unstack(fill_value=0).reset_index()

    resultados_por_mês['Ano-Mês'] = resultados_por_mês['Ano-Mês'].dt.strftime('%b-%Y')

    resultados_por_mês = resultados_por_mês.melt(id_vars=['Ano-Mês'], value_vars=['Vitória', 'Derrota'], var_name='Resultado', value_name='Quantidade')

    fig = px.line(resultados_por_mês, x='Ano-Mês', y='Quantidade', color='Resultado',
                title='Vitórias e Derrotas do Detroit Pistons por mês (Temporadas 23/24 e 24/25)',
                labels={'Ano-Mês': 'Mês', 'Quantidade': 'Quantidade'},
                color_discrete_map={'Vitória': 'green', 'Derrota': 'red'})

    fig.update_layout(xaxis=dict(type='category'))

    fig.write_image('static/dashboards/line/resultados_por_mês.png')
