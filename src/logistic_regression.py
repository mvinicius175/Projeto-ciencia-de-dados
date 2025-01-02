import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go
import os

# Função para processar cada jogador
def process_player(file_path):
    data = pd.read_csv(file_path)

    # Define independent variables (features) and dependent variable (target)
    X = data[['MIN', 'FGA', 'TOV']]
    y = data['PTS']

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Ensure the target variable is binary
    y_train = (y_train > y_train.median()).astype(int)
    y_test = (y_test > y_test.median()).astype(int)

    # Initialize and fit the logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    fig_cm = px.imshow(cm, text_auto=True, labels=dict(x="Predicted", y="Actual", color="Count"))
    fig_cm.update_layout(title_text='Confusion Matrix')
    os.makedirs('dashboards/confusion', exist_ok=True)
    fig_cm.write_html(f"dashboards/confusion/{file_path.split('/')[-1].split('.')[0]}_confusion_matrix.html")

    # ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
    roc_auc = auc(fpr, tpr)

    fig_roc = go.Figure()
    fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC curve (area = {roc_auc:.2f})'))
    fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', line=dict(dash='dash'), name='Random'))
    fig_roc.update_layout(title='Receiver Operating Characteristic', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
    os.makedirs('dashboards/roc', exist_ok=True)
    fig_roc.write_html(f"dashboards/roc/{file_path.split('/')[-1].split('.')[0]}_roc_curve.html")

# Lista de arquivos dos jogadores
player_files = [
    'data/exported/cunningham_games_table_all_seasons.csv',
    'data/exported/ivey_games_table_all_seasons.csv',
    'data/exported/duren_games_table_all_seasons.csv'
]

# Processar cada jogador
for file in player_files:
    process_player(file)
