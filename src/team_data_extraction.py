from nba_api.stats.endpoints import teamgamelog, commonteamroster
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

detroit_pistons = [team for team in nba_teams if team['full_name'] == 'Detroit Pistons'][0]
detroit_pistons_id = detroit_pistons['id']

team_game_log_23_24 = teamgamelog.TeamGameLog(team_id=detroit_pistons_id, season="2023/24")
detroit_pistons_games_23_24 = team_game_log_23_24.get_data_frames()[0]
print(detroit_pistons_games_23_24.head())

team_game_log_24_25 = teamgamelog.TeamGameLog(team_id=detroit_pistons_id, season="2024/25")
detroit_pistons_games_24_25 = team_game_log_24_25.get_data_frames()[0]
print(detroit_pistons_games_24_25.head())

detroit_pistons_games_23_24.to_csv('data/detroit_pistons_games_23_24.csv', index=False)
detroit_pistons_games_24_25.to_csv('data/detroit_pistons_games_24_25.csv', index=False)
