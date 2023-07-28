import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('Merged/cleaned_merged_all.csv')
team_stats = df.groupby('homeTeam.shortName').agg(
    home_wins=('winnerCode', lambda x: sum(x==1)),
    home_losses=('winnerCode', lambda x: sum(x==3)),
    home_draws=('winnerCode', lambda x: sum(x==2)),
    home_games=('winnerCode', 'count')
).reset_index()

team_stats = team_stats.rename(columns={'homeTeam.shortName': 'team.shortName'})

away_team_stats = df.groupby('awayTeam.shortName').agg(
    away_wins=('winnerCode', lambda x: sum(x==3)),
    away_losses=('winnerCode', lambda x: sum(x==1)),
    away_draws=('winnerCode', lambda x: sum(x==2)),
    away_games=('winnerCode', 'count')
).reset_index()

away_team_stats = away_team_stats.rename(columns={'awayTeam.shortName': 'team.shortName'})

team_stats = pd.merge(team_stats, away_team_stats, on='team.shortName', how='outer')
team_stats.fillna(0, inplace=True)

team_stats['total_games'] = team_stats['home_games'] + team_stats['away_games']
team_stats['total_wins'] = team_stats['home_wins'] + team_stats['away_wins']
team_stats['win_rate'] = team_stats['total_wins'] / team_stats['total_games']
team_stats.to_csv('stats.csv')
def create_features(home_team, away_team):
    home_team_stats = team_stats[team_stats['team.shortName'] == home_team]
    away_team_stats = team_stats[team_stats['team.shortName'] == away_team]
    features = (home_team_stats.iloc[:, 1:].values - away_team_stats.iloc[:, 1:].values).flatten()
    return features

X = df.apply(lambda row: create_features(row['homeTeam.shortName'], row['awayTeam.shortName']), axis=1, result_type='expand')
y = df['winnerCode']

models = {
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=80),
    "GradientBoosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=80),
    "SVC": SVC(random_state=80),
    "DecisionTree": DecisionTreeClassifier(random_state=80),
    "KNN": KNeighborsClassifier(),
    "NaiveBayes": GaussianNB(),
    "AdaBoost": AdaBoostClassifier(random_state=80),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=80),
    "LightGBM": LGBMClassifier(random_state=80),
    "CatBoost": CatBoostClassifier(verbose=0, random_state=80),
}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

# Handle imbalanced classes using SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Loop over models, fit to data, predict and print accuracy
for model_name, model in models.items():
    print(f"Training {model_name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} accuracy: {accuracy*100:.2f}%\n")