import pandas as pd

def clean_data():
    cunningham_23_24        = pd.read_csv('data/raw/cade_cunningham_stats_23_24.csv')
    cunningham_24_25        = pd.read_csv('data/raw/cade_cunningham_stats_24_25.csv')
    cunningham_all_seasons  = pd.read_csv('data/raw/cade_cunningham_all_seasons_games.csv')
    ivey_23_24              = pd.read_csv('data/raw/jaden_ivey_stats_23_24.csv')
    ivey_24_25              = pd.read_csv('data/raw/jaden_ivey_stats_24_25.csv')
    ivey_all_seasons        = pd.read_csv('data/raw/jaden_ivey_all_seasons_games.csv')
    duren_23_24             = pd.read_csv('data/raw/jalen_duren_stats_23_24.csv')
    duren_24_25             = pd.read_csv('data/raw/jalen_duren_stats_24_25.csv')
    duren_all_seasons       = pd.read_csv('data/raw/jalen_duren_all_seasons_games.csv')
    pistons_23_24           = pd.read_csv('data/raw/detroit_pistons_games_23_24.csv')
    pistons_24_25           = pd.read_csv('data/raw/detroit_pistons_games_24_25.csv')
    pistons_21_22           = pd.read_csv('data/raw/detroit_pistons_games_21_22.csv')
    pistons_22_23           = pd.read_csv('data/raw/detroit_pistons_games_22_23.csv')
    west_conference         = pd.read_csv('data/raw/west_conference.csv')
    east_conference         = pd.read_csv('data/raw/east_conference.csv')
    cunningham_profile      = pd.read_csv('data/raw/Cade_Cunningham_profile.csv')
    ivey_profile            = pd.read_csv('data/raw/Jaden_Ivey_profile.csv')
    duren_profile           = pd.read_csv('data/raw/Jalen_Duren_profile.csv')

    # Verificar dados ausentes
    missing_data_cunningham = cunningham_23_24.isnull().sum() + cunningham_24_25.isnull().sum() + cunningham_all_seasons.isnull().sum()
    missing_data_ivey = ivey_23_24.isnull().sum() + ivey_24_25.isnull().sum() + ivey_all_seasons.isnull().sum()
    missing_data_duren = duren_23_24.isnull().sum() + duren_24_25.isnull().sum() + duren_all_seasons.isnull().sum()
    missing_data_pistons = pistons_23_24.isnull().sum() + pistons_24_25.isnull().sum() + pistons_21_22.isnull().sum() + pistons_22_23.isnull().sum()
    missing_data_east = east_conference.isnull().sum()
    missing_data_west = west_conference.isnull().sum()

    if missing_data_cunningham.any() > 0:
        print("Cunningham datasets have missing data.")
    if missing_data_ivey.any() > 0:
        print("Ivey datasets have missing data.")
    if missing_data_duren.any() > 0:
        print("Duren datasets have missing data.")
    if missing_data_pistons.any() > 0:
        print("Pistons datasets have missing data.")
    if missing_data_east.any() > 0:
        print("East conference dataset has missing data.")
    if missing_data_west.any() > 0:
        print("West conference dataset has missing data.")

    # Lidar com dados ausentes
    def handle_missing_data(df):
        return df.dropna()

    if missing_data_cunningham.any():
        cunningham_23_24 = handle_missing_data(cunningham_23_24)
        cunningham_24_25 = handle_missing_data(cunningham_24_25)
        cunningham_all_seasons = handle_missing_data(cunningham_all_seasons)
    if missing_data_ivey.any():
        ivey_23_24 = handle_missing_data(ivey_23_24)
        ivey_24_25 = handle_missing_data(ivey_24_25)
        ivey_all_seasons = handle_missing_data(ivey_all_seasons)
    if missing_data_duren.any():
        duren_23_24 = handle_missing_data(duren_23_24)
        duren_24_25 = handle_missing_data(duren_24_25)
        duren_all_seasons = handle_missing_data(duren_all_seasons)
    if missing_data_pistons.any():
        pistons_23_24 = handle_missing_data(pistons_23_24)
        pistons_24_25 = handle_missing_data(pistons_24_25)
        pistons_21_22 = handle_missing_data(pistons_21_22)
        pistons_22_23 = handle_missing_data(pistons_22_23)

    # Verificar valores duplicados
    redundant_data_cunningham = cunningham_23_24.duplicated().sum() + cunningham_24_25.duplicated().sum() + cunningham_all_seasons.duplicated().sum()
    redundant_data_ivey = ivey_23_24.duplicated().sum() + ivey_24_25.duplicated().sum() + ivey_all_seasons.duplicated().sum()
    redundant_data_duren = duren_23_24.duplicated().sum() + duren_24_25.duplicated().sum() + duren_all_seasons.duplicated().sum()
    redundant_data_pistons = pistons_23_24.duplicated().sum() + pistons_24_25.duplicated().sum() + pistons_21_22.duplicated().sum() + pistons_22_23.duplicated().sum()
    redundant_data_east = east_conference.duplicated().sum()
    redundant_data_west = west_conference.duplicated().sum()

    if redundant_data_cunningham > 0:
        print("Cunningham datasets have redundant data.")
    if redundant_data_ivey > 0:
        print("Ivey datasets have redundant data.")
    if redundant_data_duren > 0:
        print("Duren datasets have redundant data.")
    if redundant_data_pistons > 0:
        print("Pistons datasets have redundant data.")
    if redundant_data_east > 0:
        print("East conference dataset has redundant data.")
    if redundant_data_west > 0:
        print("West conference dataset has redundant data.")

    # Lidar com dados duplicados
    def handle_duplicates(df):
        return df.drop_duplicates()

    if redundant_data_cunningham.any():
        cunningham_23_24 = handle_duplicates(cunningham_23_24)
        cunningham_24_25 = handle_duplicates(cunningham_24_25)
        cunningham_all_seasons = handle_duplicates(cunningham_all_seasons)
    if redundant_data_ivey.any():
        ivey_23_24 = handle_duplicates(ivey_23_24)
        ivey_24_25 = handle_duplicates(ivey_24_25)
        ivey_all_seasons = handle_duplicates(ivey_all_seasons)
    if redundant_data_duren.any():
        duren_23_24 = handle_duplicates(duren_23_24)
        duren_24_25 = handle_duplicates(duren_24_25)
        duren_all_seasons = handle_duplicates(duren_all_seasons)
    if redundant_data_pistons.any():
        pistons_23_24 = handle_duplicates(pistons_23_24)
        pistons_24_25 = handle_duplicates(pistons_24_25)
        pistons_21_22 = handle_duplicates(pistons_21_22)
        pistons_22_23 = handle_duplicates(pistons_22_23)

    # Verificar valores negativos onde não deveria ter
    def check_negative_values(df, columns):
        return df[columns].lt(0).sum()

    negative_values_cunningham = check_negative_values(cunningham_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(cunningham_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(cunningham_all_seasons, ['PTS', 'REB', 'AST'])
    negative_values_ivey = check_negative_values(ivey_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(ivey_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(ivey_all_seasons, ['PTS', 'REB', 'AST'])
    negative_values_duren = check_negative_values(duren_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(duren_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(duren_all_seasons, ['PTS', 'REB', 'AST'])
    negative_values_pistons = check_negative_values(pistons_23_24, ['PTS', 'REB', 'AST']) + check_negative_values(pistons_24_25, ['PTS', 'REB', 'AST']) + check_negative_values(pistons_21_22, ['PTS', 'REB', 'AST']) + check_negative_values(pistons_22_23, ['PTS', 'REB', 'AST'])

    if negative_values_cunningham.any() > 0:
        print("Cunningham datasets have negative values where they shouldn't.")
    if negative_values_ivey.any() > 0:
        print("Ivey datasets have negative values where they shouldn't.")
    if negative_values_duren.any() > 0:
        print("Duren datasets have negative values where they shouldn't.")
    if negative_values_pistons.any() > 0:
        print("Pistons datasets have negative values where they shouldn't.")

    # Lidar com valores negativos
    def handle_negative_values(df, columns):
        for column in columns:
            df[column] = df[column].apply(lambda x: 0 if x < 0 else x)
        return df

    if negative_values_cunningham.any():
        cunningham_23_24 = handle_negative_values(cunningham_23_24, ['PTS', 'REB', 'AST'])
        cunningham_24_25 = handle_negative_values(cunningham_24_25, ['PTS', 'REB', 'AST'])
        cunningham_all_seasons = handle_negative_values(cunningham_all_seasons, ['PTS', 'REB', 'AST'])
    if negative_values_ivey.any():
        ivey_23_24 = handle_negative_values(ivey_23_24, ['PTS', 'REB', 'AST'])
        ivey_24_25 = handle_negative_values(ivey_24_25, ['PTS', 'REB', 'AST'])
        ivey_all_seasons = handle_negative_values(ivey_all_seasons, ['PTS', 'REB', 'AST'])
    if negative_values_duren.any():
        duren_23_24 = handle_negative_values(duren_23_24, ['PTS', 'REB', 'AST'])
        duren_24_25 = handle_negative_values(duren_24_25, ['PTS', 'REB', 'AST'])
        duren_all_seasons = handle_negative_values(duren_all_seasons, ['PTS', 'REB', 'AST'])
    if negative_values_pistons.any():
        pistons_23_24 = handle_negative_values(pistons_23_24, ['PTS', 'REB', 'AST'])
        pistons_24_25 = handle_negative_values(pistons_24_25, ['PTS', 'REB', 'AST'])
        pistons_21_22 = handle_negative_values(pistons_21_22, ['PTS', 'REB', 'AST'])
        pistons_22_23 = handle_negative_values(pistons_22_23, ['PTS', 'REB', 'AST'])

    # Verificar porcentagens que não estão entre 0 e 1
    def check_percentage_values(df, columns):
        return df[columns].apply(lambda x: (x < 0) | (x > 1)).sum()

    percentage_columns = ['FG3_PCT', 'FG_PCT', 'FT_PCT']
    percentage_values_cunningham = check_percentage_values(cunningham_23_24, percentage_columns) + check_percentage_values(cunningham_24_25, percentage_columns) + check_percentage_values(cunningham_all_seasons, percentage_columns)
    percentage_values_ivey = check_percentage_values(ivey_23_24, percentage_columns) + check_percentage_values(ivey_24_25, percentage_columns) + check_percentage_values(ivey_all_seasons, percentage_columns)
    percentage_values_duren = check_percentage_values(duren_23_24, percentage_columns) + check_percentage_values(duren_24_25, percentage_columns) + check_percentage_values(duren_all_seasons, percentage_columns)
    percentage_values_pistons = check_percentage_values(pistons_23_24, percentage_columns) + check_percentage_values(pistons_24_25, percentage_columns) + check_percentage_values(pistons_21_22, percentage_columns) + check_percentage_values(pistons_22_23, percentage_columns)

    if percentage_values_cunningham.any() > 0:
        print("Cunningham datasets have percentage values out of range.")
    if percentage_values_ivey.any() > 0:
        print("Ivey datasets have percentage values out of range.")
    if percentage_values_duren.any() > 0:
        print("Duren datasets have percentage values out of range.")
    if percentage_values_pistons.any() > 0:
        print("Pistons datasets have percentage values out of range.")

    # Lidar com porcentagens fora do intervalo
    def handle_percentage_values(df, columns):
        for column in columns:
            df[column] = df[column].apply(lambda x: 0 if x < 0 else 1 if x > 1 else x)
        return df

    if percentage_values_cunningham.any():
        cunningham_23_24 = handle_percentage_values(cunningham_23_24, percentage_columns)
        cunningham_24_25 = handle_percentage_values(cunningham_24_25, percentage_columns)
        cunningham_all_seasons = handle_percentage_values(cunningham_all_seasons, percentage_columns)
    if percentage_values_ivey.any():
        ivey_23_24 = handle_percentage_values(ivey_23_24, percentage_columns)
        ivey_24_25 = handle_percentage_values(ivey_24_25, percentage_columns)
        ivey_all_seasons = handle_percentage_values(ivey_all_seasons, percentage_columns)
    if percentage_values_duren.any():
        duren_23_24 = handle_percentage_values(duren_23_24, percentage_columns)
        duren_24_25 = handle_percentage_values(duren_24_25, percentage_columns)
        duren_all_seasons = handle_percentage_values(duren_all_seasons, percentage_columns)


    # Verificar tipos de dados
    def check_data_types(df):
        return df.dtypes
    # print("Cunningham 24-25 data types:\n", check_data_types(cunningham_24_25))
    # print("Pistons 24-25 data types:\n", check_data_types(pistons_24_25))

    # Excluindo a coluna "VIDEO_AVAILABLE" dos datasets de jogadores
    cunningham_23_24 = cunningham_23_24.drop(columns=['VIDEO_AVAILABLE'])
    cunningham_24_25 = cunningham_24_25.drop(columns=['VIDEO_AVAILABLE'])
    cunningham_all_seasons = cunningham_all_seasons.drop(columns=['VIDEO_AVAILABLE'])
    ivey_23_24 = ivey_23_24.drop(columns=['VIDEO_AVAILABLE'])
    ivey_24_25 = ivey_24_25.drop(columns=['VIDEO_AVAILABLE'])
    ivey_all_seasons = ivey_all_seasons.drop(columns=['VIDEO_AVAILABLE'])
    duren_23_24 = duren_23_24.drop(columns=['VIDEO_AVAILABLE'])
    duren_24_25 = duren_24_25.drop(columns=['VIDEO_AVAILABLE'])
    duren_all_seasons = duren_all_seasons.drop(columns=['VIDEO_AVAILABLE'])

    # Excluindo a coluna "Team_ID" dos datasets de time
    pistons_23_24 = pistons_23_24.drop(columns=['TEAM_ID'])
    pistons_24_25 = pistons_24_25.drop(columns=['TEAM_ID'])
    pistons_21_22 = pistons_21_22.drop(columns=['TEAM_ID'])
    pistons_22_23 = pistons_22_23.drop(columns=['TEAM_ID'])

    # Excluindo a coluna "VIDEO_AVAILABLE" dos datasets de time
    pistons_23_24 = pistons_23_24.drop(columns=['VIDEO_AVAILABLE'])
    pistons_24_25 = pistons_24_25.drop(columns=['VIDEO_AVAILABLE'])
    pistons_21_22 = pistons_21_22.drop(columns=['VIDEO_AVAILABLE'])
    pistons_22_23 = pistons_22_23.drop(columns=['VIDEO_AVAILABLE'])

    # Excluinto a coluna "SEASON_ID" dos datasets de time
    pistons_23_24 = pistons_23_24.drop(columns=['SEASON_ID'])
    pistons_24_25 = pistons_24_25.drop(columns=['SEASON_ID'])
    pistons_21_22 = pistons_21_22.drop(columns=['SEASON_ID'])
    pistons_22_23 = pistons_22_23.drop(columns=['SEASON_ID'])

    # Excluindo a coluna "TEAM_ABBREVIATION" dos datasets de time
    pistons_23_24 = pistons_23_24.drop(columns=['TEAM_ABBREVIATION'])
    pistons_24_25 = pistons_24_25.drop(columns=['TEAM_ABBREVIATION'])
    pistons_21_22 = pistons_21_22.drop(columns=['TEAM_ABBREVIATION'])
    pistons_22_23 = pistons_22_23.drop(columns=['TEAM_ABBREVIATION'])

    # Excluindo a coluna "TEAM_NAME" dos datasets de time
    pistons_23_24 = pistons_23_24.drop(columns=['TEAM_NAME'])
    pistons_24_25 = pistons_24_25.drop(columns=['TEAM_NAME'])
    pistons_21_22 = pistons_21_22.drop(columns=['TEAM_NAME'])
    pistons_22_23 = pistons_22_23.drop(columns=['TEAM_NAME'])

    # Excluindo a coluna "Conference" dos datasets de conferencia
    west_conference = west_conference.drop(columns=['Conference'])
    east_conference = east_conference.drop(columns=['Conference'])

    # Convertendo o peso dos jogadores de Pounds para Quilogramas
    def pounds_to_kg(pounds):
        return round(pounds * 0.453592, 2)

    cunningham_profile['Peso'] = cunningham_profile['Peso'].apply(pounds_to_kg)
    ivey_profile['Peso'] = ivey_profile['Peso'].apply(pounds_to_kg)
    duren_profile['Peso'] = duren_profile['Peso'].apply(pounds_to_kg)

    # Convertendo a altura dos jogadores de feets para metros
    def feet_inches_to_meters(height):
        feet, inches = map(int, height.split('-'))
        return round(feet * 0.3048 + inches * 0.0254, 2)

    cunningham_profile['Altura'] = cunningham_profile['Altura'].apply(feet_inches_to_meters)
    ivey_profile['Altura'] = ivey_profile['Altura'].apply(feet_inches_to_meters)
    duren_profile['Altura'] = duren_profile['Altura'].apply(feet_inches_to_meters)

    # Salvar dados limpos
    cunningham_23_24.to_csv('data/processed/cade_cunningham_stats_23_24.csv', index=False)
    cunningham_24_25.to_csv('data/processed/cade_cunningham_stats_24_25.csv', index=False)
    cunningham_all_seasons.to_csv('data/processed/cade_cunningham_all_seasons_games.csv', index=False)
    ivey_23_24.to_csv('data/processed/jaden_ivey_stats_23_24.csv', index=False)
    ivey_24_25.to_csv('data/processed/jaden_ivey_stats_24_25.csv', index=False)
    ivey_all_seasons.to_csv('data/processed/jaden_ivey_all_seasons_games.csv', index=False)
    duren_23_24.to_csv('data/processed/jalen_duren_stats_23_24.csv', index=False)
    duren_24_25.to_csv('data/processed/jalen_duren_stats_24_25.csv', index=False)
    duren_all_seasons.to_csv('data/processed/jalen_duren_all_seasons_games.csv', index=False)
    pistons_23_24.to_csv('data/processed/detroit_pistons_games_23_24.csv', index=False)
    pistons_24_25.to_csv('data/processed/detroit_pistons_games_24_25.csv', index=False)
    pistons_21_22.to_csv('data/processed/detroit_pistons_games_21_22.csv', index=False)
    pistons_22_23.to_csv('data/processed/detroit_pistons_games_22_23.csv', index=False)
    west_conference.to_csv('data/processed/west_conference.csv', index=False)
    east_conference.to_csv('data/processed/east_conference.csv', index=False)
    cunningham_profile.to_csv('data/processed/Cade_Cunningham_profile.csv', index=False)
    ivey_profile.to_csv('data/processed/Jaden_Ivey_profile.csv', index=False)
    duren_profile.to_csv('data/processed/Jalen_Duren_profile.csv', index=False)

