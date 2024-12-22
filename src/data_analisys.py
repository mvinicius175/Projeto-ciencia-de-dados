import pandas as pd


cunningham_23_24 = pd.read_csv('data/processed/cade_cunningham_stats_23_24.csv')
cunningham_24_25 = pd.read_csv('data/processed/cade_cunningham_stats_24_25.csv')
ivey_23_24       = pd.read_csv('data/processed/jaden_ivey_stats_23_24.csv')
ivey_24_25       = pd.read_csv('data/processed/jaden_ivey_stats_24_25.csv')
duren_23_24      = pd.read_csv('data/processed/jalen_duren_stats_23_24.csv')
duren_24_25      = pd.read_csv('data/processed/jalen_duren_stats_24_25.csv')
pistons_23_24    = pd.read_csv('data/processed/detroit_pistons_games_23_24.csv')
pistons_24_25    = pd.read_csv('data/processed/detroit_pistons_games_24_25.csv')
west_conference  = pd.read_csv('data/processed/west_conference.csv')
east_conference  = pd.read_csv('data/processed/east_conference.csv')

##########################################################################################################
# Filtrar jogos em casa e fora
home_games_24_25 = pistons_24_25[pistons_24_25['MATCHUP'].str.contains('@') == False]
away_games_24_25 = pistons_24_25[pistons_24_25['MATCHUP'].str.contains('@')]
home_games_23_24 = pistons_23_24[pistons_23_24['MATCHUP'].str.contains('@') == False]
away_games_23_24 = pistons_23_24[pistons_23_24['MATCHUP'].str.contains('@')]

# Contar vitórias
total_wins_24_25 = pistons_24_25[pistons_24_25['WL'] == 'W'].shape[0]
home_wins_24_25  = home_games_24_25[home_games_24_25['WL'] == 'W'].shape[0]
away_wins_24_25  = away_games_24_25[away_games_24_25['WL'] == 'W'].shape[0]
total_wins_23_24 = pistons_23_24[pistons_23_24['WL'] == 'W'].shape[0]
home_wins_23_24  = home_games_23_24[home_games_23_24['WL'] == 'W'].shape[0]
away_wins_23_24  = away_games_23_24[away_games_23_24['WL'] == 'W'].shape[0]

# Contar derrotas
total_losses_24_25 = pistons_24_25[pistons_24_25['WL'] == 'L'].shape[0]
home_losses_24_25  = home_games_24_25[home_games_24_25['WL'] == 'L'].shape[0]
away_losses_24_25  = away_games_24_25[away_games_24_25['WL'] == 'L'].shape[0]
total_losses_23_24 = pistons_23_24[pistons_23_24['WL'] == 'L'].shape[0]
home_losses_23_24  = home_games_23_24[home_games_23_24['WL'] == 'L'].shape[0]
away_losses_23_24  = away_games_23_24[away_games_23_24['WL'] == 'L'].shape[0]

data_pistons_24_25 = {
	'Total Wins':   [total_wins_24_25],
	'Home Wins':    [home_wins_24_25],
	'Away Wins':    [away_wins_24_25],
	'Total Losses': [total_losses_24_25],
	'Home Losses':  [home_losses_24_25],
	'Away Losses':  [away_losses_24_25]
}
data_pistons_23_24 = {
	'Total Wins':   [total_wins_23_24],
	'Home Wins':    [home_wins_23_24],
	'Away Wins':    [away_wins_23_24],
	'Total Losses': [total_losses_23_24],
	'Home Losses':  [home_losses_23_24],
	'Away Losses':  [away_losses_23_24]
}
pistons_23_24_summary = pd.DataFrame(data_pistons_23_24)
pistons_23_24_summary.to_csv('data/exported/pistons_23_24_summary.csv', index=False)
pistons_24_25_summary = pd.DataFrame(data_pistons_24_25)
pistons_24_25_summary.to_csv('data/exported/pistons_24_25_summary.csv', index=False)

##########################################################################################################

total_points_23_24      = pistons_23_24['PTS'].sum()
total_points_24_25      = pistons_24_25['PTS'].sum()
total_assists_23_24     = pistons_23_24['AST'].sum()
total_assists_24_25     = pistons_24_25['AST'].sum()
total_rebounds_23_24    = pistons_23_24['REB'].sum()
total_rebounds_24_25    = pistons_24_25['REB'].sum()
total_3pointers_23_24   = pistons_23_24['FG3M'].sum()
total_3pointers_24_25   = pistons_24_25['FG3M'].sum()
total_home_losses_23_24 = home_games_23_24[home_games_23_24['WL'] == 'L'].shape[0]
total_home_losses_24_25 = home_games_24_25[home_games_24_25['WL'] == 'L'].shape[0]
total_away_losses_23_24 = away_games_23_24[away_games_23_24['WL'] == 'L'].shape[0]
total_away_losses_24_25 = away_games_24_25[away_games_24_25['WL'] == 'L'].shape[0]

data_pistons_pt1_23_24 = {
    'Total Points 23-24':       [total_points_23_24],
    'Total Assists 23-24':      [total_assists_23_24],
    'Total Rebounds 23-24':     [total_rebounds_23_24],
    'Total 3 Points 23-24':     [total_3pointers_23_24],
    'Total Home Losses 23-24':  [total_home_losses_23_24],
    'Total Away Losses 23-24':  [total_away_losses_23_24]
}
data_pistons_pt1_24_25 = {
    'Total Points 24-25':       [total_points_24_25],
    'Total Assists 24-25':      [total_assists_24_25],
    'Total Rebounds 24-25':     [total_rebounds_24_25],
    'Total 3 Points 24-25':     [total_3pointers_24_25],
    'Total Home Losses 24-25':  [total_home_losses_24_25],
    'Total Away Losses 24-25':  [total_away_losses_24_25]

}
pistons_summary_23_24_pt1 = pd.DataFrame(data_pistons_23_24)
pistons_summary_23_24_pt1.to_csv('data/exported/pistons_summary_23_24_pt1_.csv', index=False)
pistons_summary_24_25_pt1 = pd.DataFrame(data_pistons_24_25)
pistons_summary_24_25_pt1.to_csv('data/exported/pistons_summary_24_25_pt1.csv', index=False)

##########################################################################################################

total_rebounds_23_24           = pistons_23_24['REB'].sum()
total_rebounds_24_25           = pistons_24_25['REB'].sum()
total_offensive_rebounds_23_24 = pistons_23_24['OREB'].sum()
total_offensive_rebounds_24_25 = pistons_24_25['OREB'].sum()
total_defensive_rebounds_23_24 = pistons_23_24['DREB'].sum()
total_defensive_rebounds_24_25 = pistons_24_25['DREB'].sum()
total_points_23_24             = pistons_23_24['PTS'].sum()
total_points_24_25             = pistons_24_25['PTS'].sum()
total_2pointers_23_24          = pistons_23_24['FGM'].sum()
total_2pointers_24_25          = pistons_24_25['FGM'].sum()
total_3pointers_23_24          = pistons_23_24['FG3M'].sum()
total_3pointers_24_25          = pistons_24_25['FG3M'].sum()
total_free_throws_23_24        = pistons_23_24['FTM'].sum()
total_free_throws_24_25        = pistons_24_25['FTM'].sum()

data_pistons_pt2_23_24 = {
    'Total Rebounds 23-24':           [total_rebounds_23_24],
    'Total Offensive Rebounds 23-24': [total_offensive_rebounds_23_24],
    'Total Defensive Rebounds 23-24': [total_defensive_rebounds_23_24],
    'Total Points 23-24':             [total_points_23_24],
    'Total 2 Pointers 23-24':         [total_2pointers_23_24],
    'Total 3 Pointers 23-24':         [total_3pointers_23_24],
    'Total Free Throws 23-24':        [total_free_throws_23_24]
}
data_pistons_pt2_24_25 = {
    'Total Rebounds 24-25':           [total_rebounds_24_25],
    'Total Offensive Rebounds 24-25': [total_offensive_rebounds_24_25],
    'Total Defensive Rebounds 24-25': [total_defensive_rebounds_24_25],
    'Total Points 24-25':             [total_points_24_25],
    'Total 2 Pointers 24-25':         [total_2pointers_24_25],
    'Total 3 Pointers 24-25':         [total_3pointers_24_25],
    'Total Free Throws 24-25':        [total_free_throws_24_25]

}
pistons_summary_23_24_pt2 = pd.DataFrame(data_pistons_pt2_23_24)
pistons_summary_23_24_pt2.to_csv('data/exported/pistons_summary_23_24_pt2.csv', index=False)
pistons_summary_24_25_pt2 = pd.DataFrame(data_pistons_pt2_24_25)
pistons_summary_24_25_pt2.to_csv('data/exported/pistons_summary_24_25_pt2.csv', index=False)

##########################################################################################################

total_steals_23_24         = pistons_23_24['STL'].sum()
total_steals_24_25         = pistons_24_25['STL'].sum()
total_blocks_23_24         = pistons_23_24['BLK'].sum()
total_blocks_24_25         = pistons_24_25['BLK'].sum()
total_turnovers_23_24      = pistons_23_24['TOV'].sum()
total_turnovers_24_25      = pistons_24_25['TOV'].sum()
total_personal_fouls_23_24 = pistons_23_24['PF'].sum()
total_personal_fouls_24_25 = pistons_24_25['PF'].sum()

data_pistons_defense_23_24 = {
    'Total Steals': [total_steals_23_24],
    'Total Defensive Rebounds': [total_defensive_rebounds_23_24],
    'Total Blocks': [total_blocks_23_24],
    'Total Turnovers': [total_turnovers_23_24],
    'Total Personal Fouls': [total_personal_fouls_23_24]
}
data_pistons_defense_24_25 = {
    'Total Steals': [total_steals_24_25],
    'Total Defensive Rebounds': [total_defensive_rebounds_24_25],
    'Total Blocks': [total_blocks_24_25],
    'Total Turnovers': [total_turnovers_24_25],
    'Total Personal Fouls': [total_personal_fouls_24_25]
}
pistons_defensive_summary_23_24 = pd.DataFrame(data_pistons_defense_23_24)
pistons_defensive_summary_23_24.to_csv('data/exported/pistons_defensive_summary_23_24.csv', index=False)
pistons_defensive_summary_24_25 = pd.DataFrame(data_pistons_defense_24_25)
pistons_defensive_summary_24_25.to_csv('data/exported/pistons_defensive_summary_24_25.csv', index=False)

##########################################################################################################

