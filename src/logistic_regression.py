import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import os

def run_logistic_regression():
    def process_player(file_path):
        data = pd.read_csv(file_path)

        X = data[['MIN', 'FGA', 'TOV']]
        y = data['PTS']

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        y_train = (y_train > y_train.median()).astype(int)
        y_test = (y_test > y_test.median()).astype(int)

        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        y_pred_proba = model.predict_proba(X_test)

        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)

        fig_roc = go.Figure()
        fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC curve (area = {roc_auc:.2f})'))
        fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', line=dict(dash='dash'), name='F(x) = x'))
        fig_roc.update_layout(title='Receiver Operating Characteristic', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
        os.makedirs('dashboards/roc', exist_ok=True)
        fig_roc.write_html(f"dashboards/roc/{file_path.split('/')[-1].split('.')[0]}_roc_curve.html")

    player_files = [
        'data/exported/cunningham_games_table_all_seasons.csv',
        'data/exported/ivey_games_table_all_seasons.csv',
        'data/exported/duren_games_table_all_seasons.csv'
    ]

    for file in player_files:
        process_player(file)
