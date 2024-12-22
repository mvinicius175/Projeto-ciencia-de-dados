from nba_api.stats.endpoints import teamgamelog, commonteamroster, LeagueStandings, LeagueGameLog
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog

nba_teams = teams.get_teams()

detroit_pistons = [team for team in nba_teams if team['full_name'] == 'Detroit Pistons'][0]
detroit_pistons_id = detroit_pistons['id']

# Extraindo dados de classificação por conferência
standings = LeagueStandings()
standings_data = standings.get_data_frames()[0]
selected_columns = ['TeamID', 'TeamName', 'Conference', 'WINS', 'LOSSES', 'WinPCT', 'HOME', 'ROAD', 'L10', 'CurrentStreak']
selected_standings_data = standings_data[selected_columns]

east_conference = selected_standings_data[selected_standings_data['Conference'] == 'East']
east_conference_sorted = east_conference.sort_values(by='WINS', ascending=False)

west_conference = selected_standings_data[selected_standings_data['Conference'] == 'West']
west_conference_sorted = west_conference.sort_values(by='WINS', ascending=False)

east_conference_sorted.to_csv('data/raw/east_conference.csv', index=False)
west_conference_sorted.to_csv('data/raw/west_conference.csv', index=False)


# Extraindo dados do time Detroit Pistons
def get_games_by_season(season):
    # Extraindo dados dos jogos da temporada
    game_log = LeagueGameLog(season=season)
    games = game_log.get_data_frames()[0]
    return games
games_23_24 = get_games_by_season("2023-24")
games_24_25 = get_games_by_season("2024-25")
detroit_pistons_games_23_24 = games_23_24[games_23_24["TEAM_NAME"] == "Detroit Pistons"]
detroit_pistons_games_24_25 = games_24_25[games_24_25["TEAM_NAME"] == "Detroit Pistons"]


detroit_pistons_games_23_24.to_csv('data/raw/detroit_pistons_games_23_24.csv', index=False)
detroit_pistons_games_24_25.to_csv('data/raw/detroit_pistons_games_24_25.csv', index=False)

# Extraindo dados dos jogadores do time
players = ['Cade Cunningham', 'Jalen Duren', 'Jaden Ivey']

player_stats_23_24 = {}
player_stats_24_25 = {}

for player in players:
    player_id = commonteamroster.CommonTeamRoster(team_id=detroit_pistons_id, season="2023-24").get_data_frames()[0]
    player_id = player_id[player_id['PLAYER'].str.contains(player)]['PLAYER_ID'].values[0]

    player_game_log_23_24 = playergamelog.PlayerGameLog(player_id=player_id, season="2023-24")
    player_stats_23_24[player] = player_game_log_23_24.get_data_frames()[0]

    player_game_log_24_25 = playergamelog.PlayerGameLog(player_id=player_id, season="2024-25")
    player_stats_24_25[player] = player_game_log_24_25.get_data_frames()[0]

for player in players:
    player_stats_23_24[player].to_csv(f'data/raw/{player.lower().replace(" ", "_")}_stats_23_24.csv', index=False)
    player_stats_24_25[player].to_csv(f'data/raw/{player.lower().replace(" ", "_")}_stats_24_25.csv', index=False)

