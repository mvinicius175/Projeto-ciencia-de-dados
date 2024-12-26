import pandas as pd


cunningham_23_24    = pd.read_csv('data/processed/cade_cunningham_stats_23_24.csv')
cunningham_24_25    = pd.read_csv('data/processed/cade_cunningham_stats_24_25.csv')
ivey_23_24          = pd.read_csv('data/processed/jaden_ivey_stats_23_24.csv')
ivey_24_25          = pd.read_csv('data/processed/jaden_ivey_stats_24_25.csv')
duren_23_24         = pd.read_csv('data/processed/jalen_duren_stats_23_24.csv')
duren_24_25         = pd.read_csv('data/processed/jalen_duren_stats_24_25.csv')
pistons_23_24       = pd.read_csv('data/processed/detroit_pistons_games_23_24.csv')
pistons_24_25       = pd.read_csv('data/processed/detroit_pistons_games_24_25.csv')
west_conference     = pd.read_csv('data/processed/west_conference.csv')
east_conference     = pd.read_csv('data/processed/east_conference.csv')
cunningham_profile  = pd.read_csv('data/processed/Cade_Cunningham_profile.csv')
ivey_profile        = pd.read_csv('data/processed/Jaden_Ivey_profile.csv')
duren_profile       = pd.read_csv('data/processed/Jalen_Duren_profile.csv')

##########################################################################################################
# Filtrar jogos em casa e fora
home_games_24_25 = pistons_24_25[pistons_24_25['MATCHUP'].str.contains('@') == False]
road_games_24_25 = pistons_24_25[pistons_24_25['MATCHUP'].str.contains('@')]
home_games_23_24 = pistons_23_24[pistons_23_24['MATCHUP'].str.contains('@') == False]
road_games_23_24 = pistons_23_24[pistons_23_24['MATCHUP'].str.contains('@')]

# Contar vitórias
total_wins_24_25 = pistons_24_25[pistons_24_25['WL'] == 'W'].shape[0]
home_wins_24_25  = home_games_24_25[home_games_24_25['WL'] == 'W'].shape[0]
road_wins_24_25  = road_games_24_25[road_games_24_25['WL'] == 'W'].shape[0]
total_wins_23_24 = pistons_23_24[pistons_23_24['WL'] == 'W'].shape[0]
home_wins_23_24  = home_games_23_24[home_games_23_24['WL'] == 'W'].shape[0]
road_wins_23_24  = road_games_23_24[road_games_23_24['WL'] == 'W'].shape[0]

# Contar derrotas
total_losses_24_25 = pistons_24_25[pistons_24_25['WL'] == 'L'].shape[0]
home_losses_24_25  = home_games_24_25[home_games_24_25['WL'] == 'L'].shape[0]
road_losses_24_25  = road_games_24_25[road_games_24_25['WL'] == 'L'].shape[0]
total_losses_23_24 = pistons_23_24[pistons_23_24['WL'] == 'L'].shape[0]
home_losses_23_24  = home_games_23_24[home_games_23_24['WL'] == 'L'].shape[0]
road_losses_23_24  = road_games_23_24[road_games_23_24['WL'] == 'L'].shape[0]

data_pistons_24_25 = {
	'Total Wins':   [total_wins_24_25],
	'Home Wins':    [home_wins_24_25],
	'Road Wins':    [road_wins_24_25],
	'Total Losses': [total_losses_24_25],
	'Home Losses':  [home_losses_24_25],
	'Road Losses':  [road_losses_24_25]
}
data_pistons_23_24 = {
	'Total Wins':   [total_wins_23_24],
	'Home Wins':    [home_wins_23_24],
	'Road Wins':    [road_wins_23_24],
	'Total Losses': [total_losses_23_24],
	'Home Losses':  [home_losses_23_24],
	'Road Losses':  [road_losses_23_24]
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
total_road_losses_23_24 = road_games_23_24[road_games_23_24['WL'] == 'L'].shape[0]
total_road_losses_24_25 = road_games_24_25[road_games_24_25['WL'] == 'L'].shape[0]

data_pistons_pt1_23_24 = {
    'Total Points 23-24':       [total_points_23_24],
    'Total Assists 23-24':      [total_assists_23_24],
    'Total Rebounds 23-24':     [total_rebounds_23_24],
    'Total 3 Points 23-24':     [total_3pointers_23_24],
    'Total Home Losses 23-24':  [total_home_losses_23_24],
    'Total Road Losses 23-24':  [total_road_losses_23_24]
}
data_pistons_pt1_24_25 = {
    'Total Points 24-25':       [total_points_24_25],
    'Total Assists 24-25':      [total_assists_24_25],
    'Total Rebounds 24-25':     [total_rebounds_24_25],
    'Total 3 Points 24-25':     [total_3pointers_24_25],
    'Total Home Losses 24-25':  [total_home_losses_24_25],
    'Total Road Losses 24-25':  [total_road_losses_24_25]

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
    'Total Steals':             [total_steals_23_24],
    'Total Defensive Rebounds': [total_defensive_rebounds_23_24],
    'Total Blocks':             [total_blocks_23_24],
    'Total Turnovers':          [total_turnovers_23_24],
    'Total Personal Fouls':     [total_personal_fouls_23_24]
}
data_pistons_defense_24_25 = {
    'Total Steals':             [total_steals_24_25],
    'Total Defensive Rebounds': [total_defensive_rebounds_24_25],
    'Total Blocks':             [total_blocks_24_25],
    'Total Turnovers':          [total_turnovers_24_25],
    'Total Personal Fouls':     [total_personal_fouls_24_25]
}
pistons_defensive_summary_23_24 = pd.DataFrame(data_pistons_defense_23_24)
pistons_defensive_summary_23_24.to_csv('data/exported/pistons_defensive_summary_23_24.csv', index=False)
pistons_defensive_summary_24_25 = pd.DataFrame(data_pistons_defense_24_25)
pistons_defensive_summary_24_25.to_csv('data/exported/pistons_defensive_summary_24_25.csv', index=False)

##########################################################################################################
# Apresentar tabela de jogos do time
team_name_map = {
    'ATL': 'Atlanta Hawks', 'BOS': 'Boston Celtics', 'BKN': 'Brooklyn Nets', 'CHA': 'Charlotte Hornets',
    'CHI': 'Chicago Bulls', 'CLE': 'Cleveland Cavaliers', 'DAL': 'Dallas Mavericks', 'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons', 'GSW': 'Golden State Warriors', 'HOU': 'Houston Rockets', 'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers', 'LAL': 'Los Angeles Lakers', 'MEM': 'Memphis Grizzlies', 'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks', 'MIN': 'Minnesota Timberwolves', 'NOP': 'New Orleans Pelicans', 'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder', 'ORL': 'Orlando Magic', 'PHI': 'Philadelphia 76ers', 'PHX': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers', 'SAC': 'Sacramento Kings', 'SAS': 'San Antonio Spurs', 'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz', 'WAS': 'Washington Wizards'
}

def home_or_road(matchup):
    if "vs" in matchup:
        return "Home"
    elif "@" in matchup:
        return "Road"
    return None

def get_adversary(matchup):
    if "@" in matchup:
        adversario = matchup.split("@")[1].strip()
    elif "vs" in matchup:
        adversario = matchup.split("vs")[1].strip()
    adversario = adversario.split()[-1]
    return adversario

def get_adversary_name(adversary):
    return team_name_map.get(adversary, adversary)

def get_score(pts, plus_minus):
    return f"{pts} - {pts - plus_minus}"

games_23_24 = pistons_23_24
games_24_25 = pistons_24_25

games_23_24['Home or Road'] = games_23_24['MATCHUP'].apply(home_or_road)
games_23_24['Adversary'] = games_23_24['MATCHUP'].apply(get_adversary)
games_23_24['Adversary Name'] = games_23_24['Adversary'].apply(get_adversary_name)
games_23_24['Score'] = games_23_24.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)
games_24_25['Home or Road'] = games_24_25['MATCHUP'].apply(home_or_road)
games_24_25['Adversary'] = games_24_25['MATCHUP'].apply(get_adversary)
games_24_25['Adversary Name'] = games_24_25['Adversary'].apply(get_adversary_name)
games_24_25['Score'] = games_24_25.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)

games_23_24 = games_23_24[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]
games_24_25 = games_24_25[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]

games_23_24.to_csv('data/exported/pistons_games_table_23_24.csv', index=False)
games_24_25.to_csv('data/exported/pistons_games_table_24_25.csv', index=False)

##########################################################################################################

cunningham_games_23_24  = cunningham_23_24
cunningham_games_24_25  = cunningham_24_25
ivey_games_23_24        = ivey_23_24
ivey_games_24_25        = ivey_24_25
duren_games_23_24       = duren_23_24
duren_games_24_25       = duren_24_25

def transform_player_data(dataset):
    dataset['GAME_DATE'] = pd.to_datetime(dataset['GAME_DATE']).dt.strftime('%Y-%m-%d')
    dataset['Home or Road'] = dataset['MATCHUP'].apply(home_or_road)
    dataset['Adversary'] = dataset['MATCHUP'].apply(get_adversary)
    dataset['Adversary Name'] = dataset['Adversary'].apply(get_adversary_name)
    return dataset

def get_game_score(date, dataset):
    game = dataset[dataset['GAME_DATE'] == date]
    if not game.empty:
        return game.iloc[0]['Score']
    return None

cunningham_games_23_24 = transform_player_data(cunningham_games_23_24)
cunningham_games_24_25 = transform_player_data(cunningham_games_24_25)
cunningham_games_23_24['Game Score'] = cunningham_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
cunningham_games_24_25['Game Score'] = cunningham_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))

ivey_games_23_24 = transform_player_data(cunningham_games_23_24)
ivey_games_24_25 = transform_player_data(cunningham_games_24_25)
ivey_games_23_24['Game Score'] = ivey_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
ivey_games_24_25['Game Score'] = ivey_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))

duren_games_23_24 = transform_player_data(cunningham_games_23_24)
duren_games_24_25 = transform_player_data(cunningham_games_24_25)
duren_games_23_24['Game Score'] = duren_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
duren_games_24_25['Game Score'] = duren_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))


cunningham_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
cunningham_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
ivey_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
ivey_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
duren_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
duren_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]

cunningham_games_23_24.to_csv('data/exported/cunningham_games_table_23_24.csv', index=False)
cunningham_games_24_25.to_csv('data/exported/cunningham_games_table_24_25.csv', index=False)
ivey_games_23_24.to_csv('data/exported/ivey_games_table_23_24.csv', index=False)
ivey_games_24_25.to_csv('data/exported/ivey_games_table_24_25.csv', index=False)
duren_games_23_24.to_csv('data/exported/duren_games_table_23_24.csv', index=False)
duren_games_24_25.to_csv('data/exported/duren_games_table_24_25.csv', index=False)

##########################################################################################################

def search_all_columns(player_data, search_term):
    search_term = search_term.lower()
    return player_data[player_data.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)]

# Teste
search_term = 'Boston'
cunningham_search_results = search_all_columns(cunningham_games_23_24, search_term)
print(cunningham_search_results)

ivey_search_results = search_all_columns(ivey_games_23_24, search_term)
print(ivey_search_results)

duren_search_results = search_all_columns(duren_games_23_24, search_term)
print(duren_search_results)
