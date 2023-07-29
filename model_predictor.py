import joblib
import pandas as pd

def get_games(df, team_short_name, is_home=True):

    if is_home:
        games = df[df['homeTeam.shortName'] == team_short_name]
    else:
        games = df[df['awayTeam.shortName'] == team_short_name]

    games = games.drop(['match_id', 'season.name', 'season.year'], axis=1)
    return {'home_games': games.to_dict('records')} if is_home else {'away_games': games.to_dict('records')}

def median_of_games(games_dict, date_related_cols):
    data = games_dict['home_games'] if 'home_games' in games_dict else games_dict['away_games']
    df = pd.DataFrame(data)

    # Get numeric and categorical columns dynamically
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    # Exclude date related columns from numeric columns
    numeric_cols = [col for col in numeric_cols if col not in date_related_cols]

    if len(df) > 1:
        # Apply median to numeric columns
        df[numeric_cols] = df[numeric_cols].median()

        # Keep the last ones for categorical columns
        df[categorical_cols] = df[categorical_cols].iloc[-1]

    return df.to_dict('records')

def find_game(df, home_team, away_team):
    game = df[(df['homeTeam.shortName'] == home_team) & (df['awayTeam.shortName'] == away_team)]
    return game.to_dict('records')

date_related_cols = ['year', 'month', 'day', 'hour', 'minute', 'day_of_week']
homeTeam = 'Venados'
awayTeam = 'Tlaxcala'
csv_file = 'Merged/cleaned_merged_all.csv'  # replace this with your csv file's name

df = pd.read_csv(csv_file)

home_games = get_games(df, homeTeam, is_home=True)
away_games = get_games(df, awayTeam, is_home=False)

print(home_games)
print(away_games)

# Extract first game from the home and away games
first_home_game = home_games['home_games'][0] if home_games['home_games'] else None
first_away_game = away_games['away_games'][0] if away_games['away_games'] else None

# Convert these games to pandas dataframes
if first_home_game:
    df_home = pd.DataFrame([first_home_game])
else:
    df_home = pd.DataFrame()

if first_away_game:
    df_away = pd.DataFrame([first_away_game])
else:
    df_away = pd.DataFrame()

# Print out the shape of these dataframes
print("Shape of home game dataframe: ", df_home.shape)
print("Shape of away game dataframe: ", df_away.shape)

# Identify numerical columns
numeric_cols_home = df_home.select_dtypes(include='number').columns.tolist()
numeric_cols_away = df_away.select_dtypes(include='number').columns.tolist()
common_numeric_cols = list(set(numeric_cols_home).intersection(numeric_cols_away))

# Compute median for the numerical columns
merged_numerical_values = df_home[common_numeric_cols].median() + df_away[common_numeric_cols].median()

# Identify categorical columns
categorical_cols_home = df_home.select_dtypes(include='object').columns.tolist()

# Keep categorical values from df_home
merged_categorical_values = df_home[categorical_cols_home].iloc[0]

# Create a new dataframe
df_merged = pd.DataFrame([merged_numerical_values._append(merged_categorical_values)])

# Get 'match_nation' from df_home
match_nation_home = df_home['match_national'].iloc[0]

# Add 'match_nation' to df_merged
df_merged['match_national'] = match_nation_home

# Print the new dataframe
print(df_merged.shape)

# Function to preprocess the match data and make predictions
def predict_winner(df_merged, model, encoder):


    # Drop the 'winnerCode' as it's the target
    if 'winnerCode' in df_merged.columns:
        df_merged = df_merged.drop(columns=['winnerCode'])

    # Apply the same preprocessing steps used during model training
    cat_features = df_merged.select_dtypes(include=['object']).columns
    encoded_match_df = pd.DataFrame(encoder.transform(df_merged[cat_features]))
    encoded_match_df.columns = encoder.get_feature_names_out(cat_features)
    df_merged.drop(cat_features, axis=1, inplace=True)
    df_merged = pd.concat([df_merged, encoded_match_df], axis=1)

    # Make predictions using the trained model
    prediction = model.predict(df_merged)

    return prediction

df_merged = df_merged[[
    'winnerCode','tournament.name','tournament.category.name',
    'homeTeam.name','homeTeam.shortName',
    'homeTeam.userCount','homeTeam.nameCode','homeTeam.country.alpha2',
    'homeTeam.country.name','awayTeam.name','awayTeam.shortName',
    'awayTeam.nameCode','awayTeam.country.alpha2','awayTeam.country.name',
    'homeScore.current','homeScore.period1','homeScore.period2',
    'homeScore.normaltime','awayScore.current','awayScore.period1',
    'awayScore.period2','awayScore.normaltime','Home_Ball possession',
    'Away_Ball possession','Home_Total shots','Away_Total shots',
    'Home_Shots on target','Away_Shots on target','Home_Shots off target',
    'Away_Shots off target','Home_Blocked shots','Away_Blocked shots',
    'Home_Corner kicks','Away_Corner kicks','Home_Offsides',
    'Home_Fouls','Away_Fouls','Home_Yellow cards','Away_Yellow cards',
    'Home_Free kicks','Away_Free kicks','Home_Throw-ins',
    'Away_Throw-ins','Home_Goal kicks','Away_Goal kicks',
    'Home_Goalkeeper saves','Away_Goalkeeper saves','match_national',
    'match_gender','year','month','day','hour','minute','day_of_week'
]]

model = joblib.load('DecisionTree.joblib')
encoder = joblib.load('encoder.joblib')

predicted_winner = predict_winner(df_merged, model, encoder)
print(f"The predicted winner is: {predicted_winner}")




