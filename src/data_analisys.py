import pandas as pd

def analyze_data():
    cunningham_23_24       = pd.read_csv('data/processed/cade_cunningham_stats_23_24.csv')
    cunningham_24_25       = pd.read_csv('data/processed/cade_cunningham_stats_24_25.csv')
    ivey_23_24             = pd.read_csv('data/processed/jaden_ivey_stats_23_24.csv')
    ivey_24_25             = pd.read_csv('data/processed/jaden_ivey_stats_24_25.csv')
    duren_23_24            = pd.read_csv('data/processed/jalen_duren_stats_23_24.csv')
    duren_24_25            = pd.read_csv('data/processed/jalen_duren_stats_24_25.csv')
    pistons_23_24          = pd.read_csv('data/processed/detroit_pistons_games_23_24.csv')
    pistons_24_25          = pd.read_csv('data/processed/detroit_pistons_games_24_25.csv')
    pistons_21_22          = pd.read_csv('data/processed/detroit_pistons_games_21_22.csv')
    pistons_22_23          = pd.read_csv('data/processed/detroit_pistons_games_22_23.csv')
    west_conference        = pd.read_csv('data/processed/west_conference.csv')
    east_conference        = pd.read_csv('data/processed/east_conference.csv')
    cunningham_profile     = pd.read_csv('data/processed/Cade_Cunningham_profile.csv')
    ivey_profile           = pd.read_csv('data/processed/Jaden_Ivey_profile.csv')
    duren_profile          = pd.read_csv('data/processed/Jalen_Duren_profile.csv')
    cunningham_all_seasons = pd.read_csv('data/processed/cade_cunningham_all_seasons_games.csv')
    ivey_all_seasons       = pd.read_csv('data/processed/jaden_ivey_all_seasons_games.csv')
    duren_all_seasons      = pd.read_csv('data/processed/jalen_duren_all_seasons_games.csv')
    pistons_all_seasons = pd.concat([pistons_21_22, pistons_22_23, pistons_23_24, pistons_24_25], ignore_index=True)

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
    pistons_summary_23_24_pt1 = pd.DataFrame(data_pistons_pt1_23_24)
    pistons_summary_23_24_pt1.to_csv('data/exported/pistons_summary_23_24_pt1.csv', index=False)
    pistons_summary_24_25_pt1 = pd.DataFrame(data_pistons_pt1_24_25)
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
    games_all_seasons = pistons_all_seasons

    games_23_24['Home or Road'] = games_23_24['MATCHUP'].apply(home_or_road)
    games_23_24['Adversary'] = games_23_24['MATCHUP'].apply(get_adversary)
    games_23_24['Adversary Name'] = games_23_24['Adversary'].apply(get_adversary_name)
    games_23_24['Score'] = games_23_24.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)
    games_24_25['Home or Road'] = games_24_25['MATCHUP'].apply(home_or_road)
    games_24_25['Adversary'] = games_24_25['MATCHUP'].apply(get_adversary)
    games_24_25['Adversary Name'] = games_24_25['Adversary'].apply(get_adversary_name)
    games_24_25['Score'] = games_24_25.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)
    games_all_seasons['Home or Road'] = games_all_seasons['MATCHUP'].apply(home_or_road)
    games_all_seasons['Adversary'] = games_all_seasons['MATCHUP'].apply(get_adversary)
    games_all_seasons['Adversary Name'] = games_all_seasons['Adversary'].apply(get_adversary_name)
    games_all_seasons['Score'] = games_all_seasons.apply(lambda row: get_score(row['PTS'], row['PLUS_MINUS']), axis=1)
    cunningham_all_seasons['Home or Road'] = cunningham_all_seasons['MATCHUP'].apply(home_or_road)
    cunningham_all_seasons['Adversary'] = cunningham_all_seasons['MATCHUP'].apply(get_adversary)
    ivey_all_seasons['Home or Road'] = ivey_all_seasons['MATCHUP'].apply(home_or_road)
    ivey_all_seasons['Adversary'] = ivey_all_seasons['MATCHUP'].apply(get_adversary)
    duren_all_seasons['Home or Road'] = duren_all_seasons['MATCHUP'].apply(home_or_road)
    duren_all_seasons['Adversary'] = duren_all_seasons['MATCHUP'].apply(get_adversary)



    games_23_24 = games_23_24[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]
    games_24_25 = games_24_25[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]
    games_all_seasons = games_all_seasons[['GAME_DATE', 'Adversary', 'Adversary Name', 'WL', 'Home or Road', 'Score']]

    games_23_24.to_csv('data/exported/pistons_games_table_23_24.csv', index=False)
    games_24_25.to_csv('data/exported/pistons_games_table_24_25.csv', index=False)
    games_all_seasons.to_csv('data/exported/pistons_games_table_all_seasons.csv', index=False)


    ##########################################################################################################

    cunningham_games_23_24       = cunningham_23_24
    cunningham_games_24_25       = cunningham_24_25
    cunningham_games_all_seasons = cunningham_all_seasons
    ivey_games_23_24             = ivey_23_24
    ivey_games_24_25             = ivey_24_25
    ivey_games_all_seasons       = ivey_all_seasons
    duren_games_23_24            = duren_23_24
    duren_games_24_25            = duren_24_25
    duren_games_all_seasons      = duren_all_seasons

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

    cunningham_games_23_24       = transform_player_data(cunningham_games_23_24)
    cunningham_games_24_25       = transform_player_data(cunningham_games_24_25)
    cunningham_games_all_seasons = transform_player_data(cunningham_games_all_seasons)
    cunningham_games_23_24['Game Score'] = cunningham_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
    cunningham_games_24_25['Game Score'] = cunningham_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))
    cunningham_games_all_seasons['Game Score'] = cunningham_games_all_seasons['GAME_DATE'].apply(lambda date: get_game_score(date, games_all_seasons))

    ivey_games_23_24 = transform_player_data(ivey_23_24)
    ivey_games_24_25 = transform_player_data(ivey_24_25)
    ivey_games_all_seasons = transform_player_data(ivey_all_seasons)
    ivey_games_23_24['Game Score'] = ivey_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
    ivey_games_24_25['Game Score'] = ivey_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))
    ivey_games_all_seasons['Game Score'] = ivey_games_all_seasons['GAME_DATE'].apply(lambda date: get_game_score(date, games_all_seasons))

    duren_games_23_24 = transform_player_data(duren_23_24)
    duren_games_24_25 = transform_player_data(duren_24_25)
    duren_games_all_seasons = transform_player_data(duren_all_seasons)
    duren_games_23_24['Game Score'] = duren_games_23_24['GAME_DATE'].apply(lambda date: get_game_score(date, games_23_24))
    duren_games_24_25['Game Score'] = duren_games_24_25['GAME_DATE'].apply(lambda date: get_game_score(date, games_24_25))
    duren_games_all_seasons['Game Score'] = duren_games_all_seasons['GAME_DATE'].apply(lambda date: get_game_score(date, games_all_seasons))


    cunningham_games_23_24 = cunningham_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    cunningham_games_24_25 = cunningham_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    ivey_games_23_24 = ivey_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    ivey_games_24_25 = ivey_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    duren_games_23_24 = duren_games_23_24[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    duren_games_24_25 = duren_games_24_25[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    cunningham_games_all_seasons_show = cunningham_games_all_seasons[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    ivey_games_all_seasons_show = ivey_games_all_seasons[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]
    duren_games_all_seasons_show = duren_games_all_seasons[['GAME_DATE','Adversary', 'Adversary Name', 'WL', 'Home or Road', 'PTS', 'REB', 'AST', 'Game Score', 'FG3A', 'FG3M', 'MIN']]

    cunningham_games_23_24.to_csv('data/exported/cunningham_games_table_23_24.csv', index=False)
    cunningham_games_24_25.to_csv('data/exported/cunningham_games_table_24_25.csv', index=False)
    ivey_games_23_24.to_csv('data/exported/ivey_games_table_23_24.csv', index=False)
    ivey_games_24_25.to_csv('data/exported/ivey_games_table_24_25.csv', index=False)
    duren_games_23_24.to_csv('data/exported/duren_games_table_23_24.csv', index=False)
    duren_games_24_25.to_csv('data/exported/duren_games_table_24_25.csv', index=False)
    cunningham_games_all_seasons.to_csv('data/exported/cunningham_games_table_all_seasons.csv', index=False)
    ivey_games_all_seasons.to_csv('data/exported/ivey_games_table_all_seasons.csv', index=False)
    duren_games_all_seasons.to_csv('data/exported/duren_games_table_all_seasons.csv', index=False)

    ##########################################################################################################

    def search_games(player_data, search_term):
        search_term = search_term.lower()
        return player_data[player_data['Adversary Name'].str.lower().str.contains(search_term)]

    search_term = input("Digite o time que deseja ver os jogos contra: ")

    cunningham_search_results = search_games(cunningham_games_all_seasons_show, search_term)
    ivey_search_results = search_games(ivey_games_all_seasons_show, search_term)
    duren_search_results = search_games(duren_games_all_seasons_show, search_term)

    if cunningham_search_results.empty and ivey_search_results.empty and duren_search_results.empty:
        print("Não encontrado. Tente novamente.")
        search_term = analyze_data()
        return search_term

    cunningham_search_results.to_csv(f'data/exported/cunningham_games_against_{search_term}.csv', index=False)
    ivey_search_results.to_csv(f'data/exported/ivey_games_against_{search_term}.csv', index=False)
    duren_search_results.to_csv(f'data/exported/duren_games_against_{search_term}.csv', index=False)

    cunningham_vs_magic = search_games(cunningham_games_all_seasons_show, 'magic')
    ivey_vs_magic = search_games(ivey_games_all_seasons_show, 'magic')
    duren_vs_magic = search_games(duren_games_all_seasons_show, 'magic')

    cunningham_vs_magic.to_csv('data/exported/cunningham_games_vs_magic.csv', index=False)
    ivey_vs_magic.to_csv('data/exported/ivey_games_vs_magic.csv', index=False)
    duren_vs_magic.to_csv('data/exported/duren_games_vs_magic.csv', index=False)

    ##########################################################################################################

    def calculate_averages(player_data):
        avg_points = player_data['PTS'].mean()
        avg_rebounds = player_data['REB'].mean()
        avg_assists = player_data['AST'].mean()
        return avg_points, avg_rebounds, avg_assists

    def calculate_medians(player_data):
        median_points = player_data['PTS'].median()
        median_rebounds = player_data['REB'].median()
        median_assists = player_data['AST'].median()
        return median_points, median_rebounds, median_assists

    def calculate_modes(player_data):
        mode_points = player_data['PTS'].mode()[0]
        mode_rebounds = player_data['REB'].mode()[0]
        mode_assists = player_data['AST'].mode()[0]
        return mode_points, mode_rebounds, mode_assists

    def calculate_below_average_percentage(player_data, avg_points, avg_rebounds, avg_assists):
        below_avg_points = (player_data['PTS'] < avg_points).mean() * 100
        below_avg_rebounds = (player_data['REB'] < avg_rebounds).mean() * 100
        below_avg_assists = (player_data['AST'] < avg_assists).mean() * 100
        return below_avg_points, below_avg_rebounds, below_avg_assists

    def calculate_below_median_percentage(player_data, median_points, median_rebounds, median_assists):
        below_median_points = (player_data['PTS'] < median_points).mean() * 100
        below_median_rebounds = (player_data['REB'] < median_rebounds).mean() * 100
        below_median_assists = (player_data['AST'] < median_assists).mean() * 100
        return below_median_points, below_median_rebounds, below_median_assists

    def calculate_below_mode_percentage(player_data, mode_points, mode_rebounds, mode_assists):
        below_mode_points = (player_data['PTS'] < mode_points).mean() * 100
        below_mode_rebounds = (player_data['REB'] < mode_rebounds).mean() * 100
        below_mode_assists = (player_data['AST'] < mode_assists).mean() * 100
        return below_mode_points, below_mode_rebounds, below_mode_assists

    def calculate_standard_deviations(player_data):
        std_points = player_data['PTS'].std()
        std_rebounds = player_data['REB'].std()
        std_assists = player_data['AST'].std()
        return std_points, std_rebounds, std_assists

    def display_player_stats(player_data, player_name):
        avg_points, avg_rebounds, avg_assists = calculate_averages(player_data)
        median_points, median_rebounds, median_assists = calculate_medians(player_data)
        mode_points, mode_rebounds, mode_assists = calculate_modes(player_data)
        below_avg_points, below_avg_rebounds, below_avg_assists = calculate_below_average_percentage(player_data, avg_points, avg_rebounds, avg_assists)
        below_median_points, below_median_rebounds, below_median_assists = calculate_below_median_percentage(player_data, median_points, median_rebounds, median_assists)
        below_mode_points, below_mode_rebounds, below_mode_assists = calculate_below_mode_percentage(player_data, mode_points, mode_rebounds, mode_assists)
        std_points, std_rebounds, std_assists = calculate_standard_deviations(player_data)
        total_games = player_data.shape[0]

        stats_data = {
            'Player Name': [player_name],
            'Total Games': [total_games],
            'Average Points': [avg_points],
            'Median Points': [median_points],
            'Mode Points': [mode_points],
            'Standard Deviation Points': [std_points],
            'Average Rebounds': [avg_rebounds],
            'Median Rebounds': [median_rebounds],
            'Mode Rebounds': [mode_rebounds],
            'Standard Deviation Rebounds': [std_rebounds],
            'Average Assists': [avg_assists],
            'Median Assists': [median_assists],
            'Mode Assists': [mode_assists],
            'Standard Deviation Assists': [std_assists],
            'Below Average Points (%)': [below_avg_points],
            'Below Average Rebounds (%)': [below_avg_rebounds],
            'Below Average Assists (%)': [below_avg_assists],
            'Below Median Points (%)': [below_median_points],
            'Below Median Rebounds (%)': [below_median_rebounds],
            'Below Median Assists (%)': [below_median_assists],
            'Below Mode Points (%)': [below_mode_points],
            'Below Mode Rebounds (%)': [below_mode_rebounds],
            'Below Mode Assists (%)': [below_mode_assists]
        }

        stats_df = pd.DataFrame(stats_data)
        stats_df.to_csv(f'data/exported/{player_name.replace(" ", "_").lower()}_stats.csv', index=False)

    display_player_stats(cunningham_games_23_24, "Cade Cunningham 23-24")
    display_player_stats(cunningham_games_24_25, "Cade Cunningham 24-25")
    display_player_stats(ivey_games_23_24, "Jaden Ivey 23-24")
    display_player_stats(ivey_games_24_25, "Jaden Ivey 24-25")
    display_player_stats(duren_games_23_24, "Jalen Duren 23-24")
    display_player_stats(duren_games_24_25, "Jalen Duren 24-25")
    display_player_stats(cunningham_games_all_seasons, "Cade Cunningham All Seasons")
    display_player_stats(ivey_games_all_seasons, "Jaden Ivey All Seasons")
    display_player_stats(duren_games_all_seasons, "Jalen Duren All Seasons")

    ##########################################################################################################

    def create_combined_dataset(player_all_seasons, player_24_25, player_name):
        total_games_all_seasons = player_all_seasons.shape[0]
        total_points_all_seasons = player_all_seasons['PTS'].sum()
        total_assists_all_seasons = player_all_seasons['AST'].sum()
        total_rebounds_all_seasons = player_all_seasons['REB'].sum()
        total_minutes_all_seasons = player_all_seasons['MIN'].sum()

        total_games_24_25 = player_24_25.shape[0]
        total_points_24_25 = player_24_25['PTS'].sum()
        total_assists_24_25 = player_24_25['AST'].sum()
        total_rebounds_24_25 = player_24_25['REB'].sum()
        total_minutes_24_25 = player_24_25['MIN'].sum()

        combined_data = {
            'Estatisticas': ['Carreira', 'Temporada Atual'],
            'Total de Jogos': [total_games_all_seasons, total_games_24_25],
            'Total de Pontos': [total_points_all_seasons, total_points_24_25],
            'Total de Assistências': [total_assists_all_seasons, total_assists_24_25],
            'Total de Rebotes': [total_rebounds_all_seasons, total_rebounds_24_25],
            'Total de Minutos em Quadra': [total_minutes_all_seasons, total_minutes_24_25]
        }

        combined_df = pd.DataFrame(combined_data)
        combined_df.to_csv(f'data/exported/{player_name.replace(" ", "_").lower()}_combined_stats.csv', index=False)

    create_combined_dataset(cunningham_games_all_seasons, cunningham_games_24_25, "Cade Cunningham")
    create_combined_dataset(ivey_games_all_seasons, ivey_games_24_25, "Jaden Ivey")
    create_combined_dataset(duren_games_all_seasons, duren_games_24_25, "Jalen Duren")

    return search_term
