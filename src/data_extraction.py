from nba_api.stats.endpoints import commonteamroster, LeagueStandings, LeagueGameLog
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
import requests
import pandas as pd
import datetime
def extract_data():
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
    games_21_22 = get_games_by_season("2021-22")
    games_22_23 = get_games_by_season("2022-23")
    detroit_pistons_games_23_24 = games_23_24[games_23_24["TEAM_NAME"] == "Detroit Pistons"]
    detroit_pistons_games_24_25 = games_24_25[games_24_25["TEAM_NAME"] == "Detroit Pistons"]
    detroit_pistons_games_21_22 = games_21_22[games_21_22["TEAM_NAME"] == "Detroit Pistons"]
    detroit_pistons_games_22_23 = games_22_23[games_22_23["TEAM_NAME"] == "Detroit Pistons"]


    detroit_pistons_games_23_24.to_csv('data/raw/detroit_pistons_games_23_24.csv', index=False)
    detroit_pistons_games_24_25.to_csv('data/raw/detroit_pistons_games_24_25.csv', index=False)
    detroit_pistons_games_21_22.to_csv('data/raw/detroit_pistons_games_21_22.csv', index=False)
    detroit_pistons_games_22_23.to_csv('data/raw/detroit_pistons_games_22_23.csv', index=False)

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

    url = "https://stats.nba.com/stats/commonplayerinfo"
    headers = {
        "Host": "stats.nba.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.nba.com",
        "Referer": "https://www.nba.com/",
        "Connection": "keep-alive",
    }

    players = {
        "Cade Cunningham": "1630595",
        "Jaden Ivey": "1631093",
        "Jalen Duren": "1631105"
    }

    def calculate_age(birthdate_str):
        birthdate = datetime.datetime.strptime(birthdate_str.split("T")[0], "%Y-%m-%d")
        today = datetime.datetime.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    player_info = []

    for player_name, player_id in players.items():
        params = {"PlayerID": player_id}
        try:
            response = requests.get(url, headers=headers, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()

            player_data = data['resultSets'][0]['rowSet'][0]
            response_headers = data['resultSets'][0]['headers']
            player_dict = dict(zip(response_headers, player_data))

            birthdate = player_dict.get("BIRTHDATE", "1900-01-01")
            idade = calculate_age(birthdate) if birthdate != "1900-01-01" else "Desconhecido"

            selected_data = {
                "ID": player_id,
                "Nome": player_dict.get("DISPLAY_FIRST_LAST"),
                "Altura": player_dict.get("HEIGHT"),
                "Peso": player_dict.get("WEIGHT"),
                "Idade": idade,
                "Experiência": player_dict.get("SEASON_EXP"),
                "Posição": player_dict.get("POSITION"),
                "Universidade": player_dict.get("SCHOOL"),
                "Salário": player_dict.get("SALARY", "Não disponível")
            }
            player_info.append(selected_data)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar dados de {player_name}: {e}")

    for player in player_info:
        player_name = player["Nome"]
        player_stats_df = pd.DataFrame([player])
        player_stats_df.to_csv(f"data/raw/{player_name.replace(' ', '_')}_profile.csv", index=False)

    # Extraindo dados dos jogos de todas as temporadas dos jogadores
    all_seasons = ["2021-22", "2022-23", "2023-24", "2024-25"]

    all_player_stats = {}

    for player in players:
        player_id = commonteamroster.CommonTeamRoster(team_id=detroit_pistons_id, season="2023-24").get_data_frames()[0]
        player_id = player_id[player_id['PLAYER'].str.contains(player)]['PLAYER_ID'].values[0]

        all_player_stats[player] = pd.DataFrame()

        for season in all_seasons:
            player_game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
            season_stats = player_game_log.get_data_frames()[0]
            season_stats['SEASON'] = season
            all_player_stats[player] = pd.concat([all_player_stats[player], season_stats], ignore_index=True)

    for player in players:
        all_player_stats[player].to_csv(f'data/raw/{player.lower().replace(" ", "_")}_all_seasons_games.csv', index=False)
