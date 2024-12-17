import pandas as pd

cunningham_23_24 = pd.read_csv('data/raw/cade_cunningham_stats_23_24.csv')
cunningham_24_25 = pd.read_csv('data/raw/cade_cunningham_stats_24_25.csv')
ivey_23_24       = pd.read_csv('data/raw/jaden_ivey_stats_23_24.csv')
ivey_24_25       = pd.read_csv('data/raw/jaden_ivey_stats_24_25.csv')
duren_23_24      = pd.read_csv('data/raw/jalen_duren_stats_23_24.csv')
duren_24_25      = pd.read_csv('data/raw/jalen_duren_stats_24_25.csv')
pistons_23_24    = pd.read_csv('data/raw/detroit_pistons_games_23_24.csv')
pistons_24_25    = pd.read_csv('data/raw/detroit_pistons_games_24_25.csv')

# Verificar dados ausentes
missing_data_cunningham = cunningham_23_24.isnull().sum() + cunningham_24_25.isnull().sum()
missing_data_ivey = ivey_23_24.isnull().sum() + ivey_24_25.isnull().sum()
missing_data_duren = duren_23_24.isnull().sum() + duren_24_25.isnull().sum()
missing_data_pistons = pistons_23_24.isnull().sum() + pistons_24_25.isnull().sum()

if missing_data_cunningham.any() > 0:
    print("Cunningham datasets have missing data.")
if missing_data_ivey.any() > 0:
    print("Ivey datasets have missing data.")
if missing_data_duren.any() > 0:
    print("Duren datasets have missing data.")
if missing_data_pistons.any() > 0:
    print("Pistons datasets have missing data.")

# Verificar valores duplicados
redundant_data_cunningham = cunningham_23_24.duplicated().sum() + cunningham_24_25.duplicated().sum()
redundant_data_ivey = ivey_23_24.duplicated().sum() + ivey_24_25.duplicated().sum()
redundant_data_duren = duren_23_24.duplicated().sum() + duren_24_25.duplicated().sum()
redundant_data_pistons = pistons_23_24.duplicated().sum() + pistons_24_25.duplicated().sum()

if redundant_data_cunningham > 0:
    print("Cunningham datasets have redundant data.")
if redundant_data_ivey > 0:
    print("Ivey datasets have redundant data.")
if redundant_data_duren > 0:
    print("Duren datasets have redundant data.")
if redundant_data_pistons > 0:
    print("Pistons datasets have redundant data.")

# Verificar valores ruidosos (outliers)
def detect_outliers(df):
    outliers = pd.DataFrame()
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers[column] = ((df[column] < lower_bound) | (df[column] > upper_bound))
    return outliers.sum()

outliers_cunningham = detect_outliers(cunningham_23_24) + detect_outliers(cunningham_24_25)
outliers_ivey = detect_outliers(ivey_23_24) + detect_outliers(ivey_24_25)
outliers_duren = detect_outliers(duren_23_24) + detect_outliers(duren_24_25)
outliers_pistons = detect_outliers(pistons_23_24) + detect_outliers(pistons_24_25)

if outliers_cunningham.any() > 0:
    print("Cunningham datasets have outliers.")
if outliers_ivey.any() > 0:
    print("Ivey datasets have outliers.")
if outliers_duren.any() > 0:
    print("Duren datasets have outliers.")
if outliers_pistons.any() > 0:
    print("Pistons datasets have outliers.")


# Lidar com valores ruidosos (outliers)
def handle_outliers(df):
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = df[column].apply(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x)
    return df

cunningham_23_24 = handle_outliers(cunningham_23_24)
cunningham_24_25 = handle_outliers(cunningham_24_25)
ivey_23_24 = handle_outliers(ivey_23_24)
ivey_24_25 = handle_outliers(ivey_24_25)
duren_23_24 = handle_outliers(duren_23_24)
duren_24_25 = handle_outliers(duren_24_25)
pistons_23_24 = handle_outliers(pistons_23_24)
pistons_24_25 = handle_outliers(pistons_24_25)

# Salvar dados limpos
cunningham_23_24.to_csv('data/processed/cade_cunningham_stats_23_24.csv', index=False)
cunningham_24_25.to_csv('data/processed/cade_cunningham_stats_24_25.csv', index=False)
ivey_23_24.to_csv('data/processed/jaden_ivey_stats_23_24.csv', index=False)
ivey_24_25.to_csv('data/processed/jaden_ivey_stats_24_25.csv', index=False)
duren_23_24.to_csv('data/processed/jalen_duren_stats_23_24.csv', index=False)
duren_24_25.to_csv('data/processed/jalen_duren_stats_24_25.csv', index=False)
pistons_23_24.to_csv('data/processed/detroit_pistons_games_23_24.csv', index=False)
pistons_24_25.to_csv('data/processed/detroit_pistons_games_24_25.csv', index=False)
