from flask import Flask, render_template
import pandas as pd

search_term = 'Default'
app = Flask(__name__)

def set_param(value):
    global search_term
    search_term = value

@app.route('/')
def index():
    west_conference = pd.read_csv('data/processed/west_conference.csv')
    east_conference = pd.read_csv('data/processed/east_conference.csv')
    pistons_summary_23_24 = pd.read_csv('data/exported/pistons_23_24_summary.csv')
    pistons_summary_24_25 = pd.read_csv('data/exported/pistons_24_25_summary.csv')
    pistons_summary_23_24_pt1 = pd.read_csv('data/exported/pistons_summary_23_24_pt1.csv')
    pistons_summary_24_25_pt1 = pd.read_csv('data/exported/pistons_summary_24_25_pt1.csv')
    pistons_summary_23_24_pt2 = pd.read_csv('data/exported/pistons_summary_23_24_pt2.csv')
    pistons_summary_24_25_pt2 = pd.read_csv('data/exported/pistons_summary_24_25_pt2.csv')
    pistons_defensive_summary_23_24 = pd.read_csv('data/exported/pistons_defensive_summary_23_24.csv')
    pistons_defensive_summary_24_25 = pd.read_csv('data/exported/pistons_defensive_summary_24_25.csv')
    cunningham_profile = pd.read_csv('data/processed/Cade_Cunningham_profile.csv')
    ivey_profile = pd.read_csv('data/processed/Jaden_Ivey_profile.csv')
    duren_profile = pd.read_csv('data/processed/Jalen_Duren_profile.csv')
    cunningham_games_table_24_25 = pd.read_csv('data/exported/cunningham_games_table_24_25.csv')
    ivey_games_table_24_25 = pd.read_csv('data/exported/ivey_games_table_24_25.csv')
    duren_games_table_24_25 = pd.read_csv('data/exported/duren_games_table_24_25.csv')
    cunningham_games_against_x = pd.read_csv(f'data/exported/cunningham_games_against_{search_term}.csv')
    ivey_games_against_x = pd.read_csv(f'data/exported/ivey_games_against_{search_term}.csv')
    duren_games_against_x = pd.read_csv(f'data/exported/duren_games_against_{search_term}.csv')
    cunningham_vs_magic = pd.read_csv('data/exported/cunningham_games_vs_magic.csv')
    ivey_vs_magic = pd.read_csv('data/exported/ivey_games_vs_magic.csv')
    duren_vs_magic = pd.read_csv('data/exported/duren_games_vs_magic.csv')
    cunningham_stats_23_24 = pd.read_csv('data/exported/cade_cunningham_23-24_stats.csv')
    cunningham_stats_24_25 = pd.read_csv('data/exported/cade_cunningham_24-25_stats.csv')
    ivey_stats_23_24 = pd.read_csv('data/exported/jaden_ivey_23-24_stats.csv')
    ivey_stats_24_25 = pd.read_csv('data/exported/jaden_ivey_24-25_stats.csv')
    duren_stats_23_24 = pd.read_csv('data/exported/jalen_duren_23-24_stats.csv')
    duren_stats_24_25 = pd.read_csv('data/exported/jalen_duren_24-25_stats.csv')
    cunningham_stats_career = pd.read_csv('data/exported/cade_cunningham_combined_stats.csv')
    ivey_stats_career = pd.read_csv('data/exported/jaden_ivey_combined_stats.csv')
    duren_stats_career = pd.read_csv('data/exported/jalen_duren_combined_stats.csv')
    ivey_predictions = pd.read_csv('data/exported/ivey_predictions.csv')
    duren_predictions = pd.read_csv('data/exported/duren_predictions.csv')
    cunningham_predictions = pd.read_csv('data/exported/cunningham_predictions.csv')



    return render_template(
        'index.html',
        east_conference=east_conference.to_html(classes='table table-striped', index=True),
        west_conference=west_conference.to_html(classes='table table-striped', index=True),
        pistons_summary_23_24=pistons_summary_23_24.to_html(classes='table table-striped', index=False),
        pistons_summary_24_25=pistons_summary_24_25.to_html(classes='table table-striped', index=False),
        pistons_summary_23_24_pt1=pistons_summary_23_24_pt1.to_html(classes='table table-striped', index=False),
        pistons_summary_24_25_pt1=pistons_summary_24_25_pt1.to_html(classes='table table-striped', index=False),
        pistons_summary_23_24_pt2=pistons_summary_23_24_pt2.to_html(classes='table table-striped', index=False),
        pistons_summary_24_25_pt2=pistons_summary_24_25_pt2.to_html(classes='table table-striped', index=False),
        pistons_defensive_summary_23_24=pistons_defensive_summary_23_24.to_html(classes='table table-striped', index=False),
        pistons_defensive_summary_24_25=pistons_defensive_summary_24_25.to_html(classes='table table-striped', index=False),
        bar_wins_losses_23_24='dashboards/bar/pistons_wins_losses_23_24.png',
        bar_wins_losses_24_25='dashboards/bar/pistons_wins_losses_24_25.png',
        histogram_wins_losses='dashboards/histogram/resultados_por_mês.png',
        pie_home_away_win_losses_23_24 = 'dashboards/pie/pistons_home_away_wins_losses_23_24.png',
        pie_home_away_win_losses_24_25 = 'dashboards/pie/pistons_home_away_wins_losses_24_25.png',
        line_wins_losses = 'dashboards/line/resultados_por_mês.png',
        scatter_points_23_24 = 'dashboards/scatter/pistons_points_23_24.png',
        scatter_points_24_25 = 'dashboards/scatter/pistons_points_24_25.png',
        cunningham_profile=cunningham_profile.to_html(classes='table table-striped', index=False),
        ivey_profile=ivey_profile.to_html(classes='table table-striped', index=False),
        duren_profile=duren_profile.to_html(classes='table table-striped', index=False),
        cunningham_games_table_24_25=cunningham_games_table_24_25.to_html(classes='table table-striped', index=False),
        ivey_games_table_24_25=ivey_games_table_24_25.to_html(classes='table table-striped', index=False),
        duren_games_table_24_25=duren_games_table_24_25.to_html(classes='table table-striped', index=False),
        cunningham_games_against_x=cunningham_games_against_x.to_html(classes='table table-striped', index=False),
        ivey_games_against_x=ivey_games_against_x.to_html(classes='table table-striped', index=False),
        duren_games_against_x=duren_games_against_x.to_html(classes='table table-striped', index=False),
        cunningham_vs_magic=cunningham_vs_magic.to_html(classes='table table-striped', index=False),
        ivey_vs_magic=ivey_vs_magic.to_html(classes='table table-striped', index=False),
        duren_vs_magic=duren_vs_magic.to_html(classes='table table-striped', index=False),
        cunningham_stats_23_24=cunningham_stats_23_24.to_html(classes='table table-striped', index=False),
        cunningham_stats_24_25=cunningham_stats_24_25.to_html(classes='table table-striped', index=False),
        ivey_stats_23_24=ivey_stats_23_24.to_html(classes='table table-striped', index=False),
        ivey_stats_24_25=ivey_stats_24_25.to_html(classes='table table-striped', index=False),
        duren_stats_23_24=duren_stats_23_24.to_html(classes='table table-striped', index=False),
        duren_stats_24_25=duren_stats_24_25.to_html(classes='table table-striped', index=False),
        cunningham_stats_career=cunningham_stats_career.to_html(classes='table table-striped', index=False),
        ivey_stats_career=ivey_stats_career.to_html(classes='table table-striped', index=False),
        duren_stats_career=duren_stats_career.to_html(classes='table table-striped', index=False),
        distribution_cunningham_ast = 'dashboards/distribution/Cunningham_AST_distribution.png',
        distribution_cunningham_pts = 'dashboards/distribution/Cunningham_PTS_distribution.png',
        distribution_cunningham_reb = 'dashboards/distribution/Cunningham_REB_distribution.png',
        distribution_duren_ast = 'dashboards/distribution/Duren_AST_distribution.png',
        distribution_duren_pts = 'dashboards/distribution/Duren_PTS_distribution.png',
        distribution_duren_reb = 'dashboards/distribution/Duren_REB_distribution.png',
        distribution_ivey_ast = 'dashboards/distribution/Ivey_AST_distribution.png',
        distribution_ivey_pts = 'dashboards/distribution/Ivey_PTS_distribution.png',
        distribution_ivey_reb = 'dashboards/distribution/Ivey_REB_distribution.png',
        box_plot = 'dashboards/box_plot/box_plot.png',
        line_cunningham_assists_probabilities='dashboards/line/cunningham_assists_probabilities.png',
        line_cunningham_points_probabilities='dashboards/line/cunningham_points_probabilities.png',
        line_cunningham_rebounds_probabilities='dashboards/line/cunningham_rebounds_probabilities.png',
        line_duren_assists_probabilities='dashboards/line/duren_assists_probabilities.png',
        line_duren_points_probabilities='dashboards/line/duren_points_probabilities.png',
        line_duren_rebounds_probabilities='dashboards/line/duren_rebounds_probabilities.png',
        line_ivey_assists_probabilities='dashboards/line/ivey_assists_probabilities.png',
        line_ivey_points_probabilities='dashboards/line/ivey_points_probabilities.png',
        line_ivey_rebounds_probabilities='dashboards/line/ivey_rebounds_probabilities.png',
        bar_cunningham_ast_probabilities='dashboards/bar/Cunningham_ast_probabilities.png',
        bar_cunningham_pts_probabilities='dashboards/bar/Cunningham_pts_probabilities.png',
        bar_cunningham_reb_probabilities='dashboards/bar/Cunningham_reb_probabilities.png',
        bar_duren_ast_probabilities='dashboards/bar/Duren_ast_probabilities.png',
        bar_duren_pts_probabilities='dashboards/bar/Duren_pts_probabilities.png',
        bar_duren_reb_probabilities='dashboards/bar/Duren_reb_probabilities.png',
        bar_ivey_ast_probabilities='dashboards/bar/Ivey_ast_probabilities.png',
        bar_ivey_pts_probabilities='dashboards/bar/Ivey_pts_probabilities.png',
        bar_ivey_reb_probabilities='dashboards/bar/Ivey_reb_probabilities.png',
        cunningham_roc_curve='dashboards/roc/cunningham_games_table_all_seasons_roc_curve.png',
        duren_roc_curve='dashboards/roc/duren_games_table_all_seasons_roc_curve.png',
        ivey_roc_curve='dashboards/roc/ivey_games_table_all_seasons_roc_curve.png',
        chart_cunningham_predictions='dashboards/predictions/cunningham_predictions.png',
        chart_duren_predictions='dashboards/predictions/duren_predictions.png',
        chart_ivey_predictions='dashboards/predictions/ivey_predictions.png',
        cunningham_predictions=cunningham_predictions.to_html(classes='table table-striped', index=False),
        ivey_predictions=ivey_predictions.to_html(classes='table table-striped', index=False),
        duren_predictions=duren_predictions.to_html(classes='table table-striped', index=False)
    )



