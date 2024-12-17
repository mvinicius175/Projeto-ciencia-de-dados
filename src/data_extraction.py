from nba_api.stats.endpoints import teamgamelog, commonteamroster
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog


nba_teams = teams.get_teams()

detroit_pistons = [team for team in nba_teams if team['full_name'] == 'Detroit Pistons'][0]
detroit_pistons_id = detroit_pistons['id']

team_game_log_23_24 = teamgamelog.TeamGameLog(team_id=detroit_pistons_id, season="2023/24")
detroit_pistons_games_23_24 = team_game_log_23_24.get_data_frames()[0]
# print(detroit_pistons_games_23_24.head())

team_game_log_24_25 = teamgamelog.TeamGameLog(team_id=detroit_pistons_id, season="2024/25")
detroit_pistons_games_24_25 = team_game_log_24_25.get_data_frames()[0]
# print(detroit_pistons_games_24_25.head())

detroit_pistons_games_23_24.to_csv('data/raw/detroit_pistons_games_23_24.csv', index=False)
detroit_pistons_games_24_25.to_csv('data/raw/detroit_pistons_games_24_25.csv', index=False)

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

