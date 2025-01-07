import pandas as pd
import plotly.express as px

def plot_histograms():
    pistons_23_24_summary = pd.read_csv('data/processed/detroit_pistons_games_23_24.csv')
    pistons_24_25_summary = pd.read_csv('data/processed/detroit_pistons_games_24_25.csv')

    pistons_both_seasons_summary = pd.concat([pistons_23_24_summary, pistons_24_25_summary], ignore_index=True)

    pistons_both_seasons_summary['Resultado'] = pistons_both_seasons_summary['WL'].apply(lambda x: 'Vitória' if x == 'W' else 'Derrota')

    pistons_both_seasons_summary['GAME_DATE'] = pd.to_datetime(pistons_both_seasons_summary['GAME_DATE'])

    pistons_both_seasons_summary['Ano-Mês'] = pistons_both_seasons_summary['GAME_DATE'].dt.to_period('M')

    resultados_por_mês = pistons_both_seasons_summary.groupby(['Ano-Mês', 'Resultado']).size().unstack(fill_value=0).reset_index()

    resultados_por_mês['Ano-Mês'] = resultados_por_mês['Ano-Mês'].dt.strftime('%b-%Y')

    fig = px.bar(resultados_por_mês, x='Ano-Mês', y=['Vitória', 'Derrota'],
                title='Vitórias e Derrotas do Detroit Pistons por mês (Temporadas 23/24 e 24/25)',
                labels={'Ano-Mês': 'Mês', 'value': 'Quantidade'},
                color_discrete_map={'Vitória': 'green', 'Derrota': 'red'})

    fig.update_layout(xaxis=dict(type='category'), barmode='group')

    fig.write_image('static/dashboards/histogram/resultados_por_mês.png')
