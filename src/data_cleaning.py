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

# Lidar com dados ausentes
def handle_missing_data(df):
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            if df[column].dtype in ['float64', 'int64']:
                df[column].fillna(df[column].mean(), inplace=True)
            else:
                df[column].fillna(df[column].mode()[0], inplace=True)
    return df

if missing_data_cunningham.any():
    cunningham_23_24 = handle_missing_data(cunningham_23_24)
    cunningham_24_25 = handle_missing_data(cunningham_24_25)
if missing_data_ivey.any():
    ivey_23_24 = handle_missing_data(ivey_23_24)
    ivey_24_25 = handle_missing_data(ivey_24_25)
if missing_data_duren.any():
    duren_23_24 = handle_missing_data(duren_23_24)
    duren_24_25 = handle_missing_data(duren_24_25)
if missing_data_pistons.any():
    pistons_23_24 = handle_missing_data(pistons_23_24)
    pistons_24_25 = handle_missing_data(pistons_24_25)

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

# Lidar com dados duplicados
def handle_duplicates(df):
    return df.drop_duplicates()

if redundant_data_cunningham.any():
    cunningham_23_24 = handle_duplicates(cunningham_23_24)
    cunningham_24_25 = handle_duplicates(cunningham_24_25)
if redundant_data_ivey.any():
    ivey_23_24 = handle_duplicates(ivey_23_24)
    ivey_24_25 = handle_duplicates(ivey_24_25)
if redundant_data_duren.any():
    duren_23_24 = handle_duplicates(duren_23_24)
    duren_24_25 = handle_duplicates(duren_24_25)
if redundant_data_pistons.any():
    pistons_23_24 = handle_duplicates(pistons_23_24)
    pistons_24_25 = handle_duplicates(pistons_24_25)

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

if outliers_cunningham.any():
    cunningham_23_24 = handle_outliers(cunningham_23_24)
    cunningham_24_25 = handle_outliers(cunningham_24_25)
if outliers_ivey.any():
    ivey_23_24 = handle_outliers(ivey_23_24)
    ivey_24_25 = handle_outliers(ivey_24_25)
if outliers_duren.any():
    duren_23_24 = handle_outliers(duren_23_24)
    duren_24_25 = handle_outliers(duren_24_25)
if outliers_pistons.any():
    pistons_23_24 = handle_outliers(pistons_23_24)
    pistons_24_25 = handle_outliers(pistons_24_25)

# Verificar tipos de dados
def check_data_types(df):
    return df.dtypes
print("Cunningham 24-25 data types:\n", check_data_types(cunningham_24_25))
print("Pistons 24-25 data types:\n", check_data_types(pistons_24_25))   # Não há necessidade de mudar o tipo de nenhuma coluna no momento

# Excluindo a coluna "VIDEO_AVAILABLE" dos datasets de jogadores
cunningham_23_24 = cunningham_23_24.drop(columns=['VIDEO_AVAILABLE'])
cunningham_24_25 = cunningham_24_25.drop(columns=['VIDEO_AVAILABLE'])
ivey_23_24 = ivey_23_24.drop(columns=['VIDEO_AVAILABLE'])
ivey_24_25 = ivey_24_25.drop(columns=['VIDEO_AVAILABLE'])
duren_23_24 = duren_23_24.drop(columns=['VIDEO_AVAILABLE'])
duren_24_25 = duren_24_25.drop(columns=['VIDEO_AVAILABLE'])

# Salvar dados limpos
cunningham_23_24.to_csv('data/processed/cade_cunningham_stats_23_24.csv', index=False)
cunningham_24_25.to_csv('data/processed/cade_cunningham_stats_24_25.csv', index=False)
ivey_23_24.to_csv('data/processed/jaden_ivey_stats_23_24.csv', index=False)
ivey_24_25.to_csv('data/processed/jaden_ivey_stats_24_25.csv', index=False)
duren_23_24.to_csv('data/processed/jalen_duren_stats_23_24.csv', index=False)
duren_24_25.to_csv('data/processed/jalen_duren_stats_24_25.csv', index=False)
pistons_23_24.to_csv('data/processed/detroit_pistons_games_23_24.csv', index=False)
pistons_24_25.to_csv('data/processed/detroit_pistons_games_24_25.csv', index=False)
