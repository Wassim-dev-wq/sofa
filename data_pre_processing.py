import re

import pandas as pd
import numpy as np
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def load_data(filename):
    df = pd.read_csv(filename)
    return df


def clean_data(df):
    # Replace empty strings with NaN
    df.replace("", np.nan, inplace=True)

    # Drop columns with missing data above a defined threshold
    threshold = 200
    missing_counts = df.isnull().sum()
    cols_to_drop = missing_counts[missing_counts > threshold].index.tolist()

    df['match_national'] = df['homeTeam.national']
    df['match_gender'] = df['homeTeam.gender']

    # Drop additional unnecessary columns
    additional_cols_to_drop = ['homeTeam.manager.shortName', 'awayTeam.manager.shortName', 'Away_Offsides',
                               'homeScore.display', 'awayScore.display', 'awayTeam.foundationDateTimestamp',
                               'homeTeam.manager.country.alpha2', 'awayTeam.manager.country.alpha2',
                               'homeTeam.manager.country.name', 'awayTeam.manager.country.name',
                               'homeTeam.manager.shortName', 'awayTeam.manager.shortName','tournament.uniqueTournament.name',
                               'homeTeam.fullName','awayTeam.fullName','homeTeam.gender', 'awayTeam.gender',
                               'awayTeam.national', 'homeTeam.national','tournament.category.alpha2', 'tournament.uniqueTournament.category.alpha2',
                               'venue.city.name', 'venue.stadium.name', 'venue.stadium.capacity', 'venue.country.alpha2',
                               'venue.country.name', 'referee.name', 'referee.yellowCards', 'referee.redCards',
                               'referee.yellowRedCards', 'referee.games', 'referee.country.alpha2', 'referee.country.name',
                               'homeTeam.venue.city.name', 'homeTeam.venue.stadium.name', 'homeTeam.venue.stadium.capacity',
                               'homeTeam.venue.id', 'homeTeam.venue.country.alpha2', 'homeTeam.venue.country.name',
                               'awayTeam.venue.city.name', 'awayTeam.venue.stadium.name', 'awayTeam.venue.stadium.capacity',
                               'awayTeam.venue.id', 'awayTeam.venue.country.alpha2', 'awayTeam.venue.country.name', 'time.injuryTime1',
                               'Home_Big chances', 'Away_Big chances', 'Home_Big chances missed', 'Away_Big chances missed',
                               'Home_Hit woodwork', 'Away_Hit woodwork', 'Home_Shots inside box', 'Away_Shots inside box',
                               'Home_Shots outside box', 'Away_Shots outside box', 'Home_Passes', 'Away_Passes',
                               'Home_Accurate passes', 'Away_Accurate passes', 'Home_Long balls', 'Away_Long balls',
                               'Home_Crosses', 'Away_Crosses', 'Home_Dribbles', 'Away_Dribbles', 'Home_Possession lost',
                               'Away_Possession lost', 'Home_Duels won', 'Away_Duels won', 'Home_Aerials won', 'Away_Aerials won',
                               'Home_Tackles', 'Away_Tackles', 'Home_Interceptions', 'Away_Interceptions', 'Home_Clearances',
                               'Away_Clearances', 'Home_Ball possession.1', 'Away_Ball possession.1', 'Home_Total shots.1',
                               'Away_Total shots.1', 'Home_Shots on target.1', 'Away_Shots on target.1', 'Home_Shots off target.1',
                               'Away_Shots off target.1', 'Home_Blocked shots.1', 'Away_Blocked shots.1', 'Home_Corner kicks.1',
                               'Away_Corner kicks.1', 'time.injuryTime2', 'Home_Offsides.1', 'Away_Offsides.1', 'Home_Yellow cards.1',
                               'Away_Yellow cards.1', 'Home_Free kicks.1', 'Away_Free kicks.1', 'Home_Throw-ins.1', 'Away_Throw-ins.1',
                               'Home_Goal kicks.1', 'Away_Goal kicks.1', 'Home_Shots inside box.1', 'Away_Shots inside box.1',
                               'Home_Shots outside box.1', 'Away_Shots outside box.1', 'Home_Goalkeeper saves.1',
                               'Away_Goalkeeper saves.1', 'Home_Passes.1', 'Away_Passes.1', 'Home_Accurate passes.1',
                               'Away_Accurate passes.1', 'Home_Long balls.1', 'Away_Long balls.1', 'Home_Crosses.1', 'Away_Crosses.1',
                               'Home_Dribbles.1', 'Away_Dribbles.1', 'Home_Possession lost.1', 'Away_Possession lost.1',
                               'Home_Duels won.1', 'Away_Duels won.1', 'Home_Aerials won.1', 'Away_Aerials won.1', 'Home_Tackles.1',
                               'Away_Tackles.1', 'Home_Interceptions.1', 'Away_Interceptions.1', 'Home_Clearances.1',
                               'Away_Clearances.1', 'Home_Ball possession.2', 'Away_Ball possession.2', 'Home_Total shots.2',
                               'Away_Total shots.2', 'Home_Shots on target.2', 'Away_Shots on target.2', 'Home_Shots off target.2',
                               'Away_Shots off target.2', 'Home_Blocked shots.2', 'Away_Blocked shots.2', 'Home_Corner kicks.2',
                               'Away_Corner kicks.2', 'Home_Offsides.2', 'Away_Offsides.2', 'Home_Yellow cards.2', 'Away_Yellow cards.2',
                               'Home_Free kicks.2', 'Away_Free kicks.2', 'Home_Throw-ins.2', 'Away_Throw-ins.2', 'Home_Goal kicks.2',
                               'Away_Goal kicks.2', 'Home_Big chances.1', 'Away_Big chances.1', 'Home_Big chances missed.1',
                               'Away_Big chances missed.1', 'Home_Hit woodwork.1', 'Away_Hit woodwork.1', 'Home_Shots inside box.2',
                               'Away_Shots inside box.2', 'Home_Shots outside box.2', 'Away_Shots outside box.2',
                               'Home_Goalkeeper saves.2', 'Away_Goalkeeper saves.2', 'Home_Passes.2', 'Away_Passes.2',
                               'Home_Accurate passes.2', 'Away_Accurate passes.2', 'Home_Long balls.2', 'Away_Long balls.2', 'Home_Crosses.2', 'Away_Crosses.2', 'Home_Dribbles.2', 'Away_Dribbles.2', 'Home_Possession lost.2', 'Away_Possession lost.2', 'Home_Duels won.2', 'Away_Duels won.2', 'Home_Aerials won.2', 'Away_Aerials won.2', 'Home_Tackles.2', 'Away_Tackles.2', 'Home_Interceptions.2', 'Away_Interceptions.2', 'Home_Clearances.2', 'Away_Clearances.2', 'Home_Counter attacks', 'Away_Counter attacks', 'Home_Counter attack shots', 'Away_Counter attack shots', 'Home_Counter attack goals', 'Away_Counter attack goals', 'Home_Counter attacks.1', 'Away_Counter attacks.1', 'Home_Counter attack shots.1', 'Away_Counter attack shots.1', 'Home_Counter attack goals.1', 'Away_Counter attack goals.1', 'Home_Big chances.2', 'Away_Big chances.2', 'Home_Counter attacks.2', 'Away_Counter attacks.2', 'Home_Counter attack shots.2', 'Away_Counter attack shots.2', 'Home_Counter attack goals.2', 'Away_Counter attack goals.2', 'Home_Big chances missed.2', 'Away_Big chances missed.2', 'homeRedCards', 'Home_Red cards', 'Away_Red cards', 'Home_Red cards.1', 'Away_Red cards.1', 'awayRedCards', 'Home_Red cards.2', 'Away_Red cards.2', 'attendance', 'roundInfo.slug', 'roundInfo.cupRoundType', 'homeScore.aggregated', 'awayScore.aggregated', 'homeScore.penalties', 'awayScore.penalties', 'homeScore.extra1', 'homeScore.extra2', 'homeScore.overtime', 'awayScore.extra1', 'awayScore.extra2', 'awayScore.overtime', 'time.injuryTime3', 'time.injuryTime4', 'Home_Total shots.3', 'Away_Total shots.3', 'Home_Shots on target.3', 'Away_Shots on target.3', 'Home_Shots off target.3', 'Away_Shots off target.3', 'Home_Blocked shots.3', 'Away_Blocked shots.3', 'Home_Yellow cards.3', 'Away_Yellow cards.3', 'Home_Free kicks.3', 'Away_Free kicks.3', 'Home_Throw-ins.3', 'Away_Throw-ins.3', 'Home_Goal kicks.3', 'Away_Goal kicks.3', 'Home_Big chances.3', 'Away_Big chances.3', 'Home_Big chances missed.3', 'Away_Big chances missed.3', 'Home_Shots inside box.3', 'Away_Shots inside box.3', 'Home_Shots outside box.3', 'Away_Shots outside box.3', 'Home_Goalkeeper saves.3', 'Away_Goalkeeper saves.3', 'Home_Passes.3', 'Away_Passes.3', 'Home_Accurate passes.3', 'Away_Accurate passes.3', 'Home_Long balls.3', 'Away_Long balls.3', 'Home_Crosses.3', 'Away_Crosses.3', 'Home_Dribbles.3', 'Away_Dribbles.3', 'Home_Possession lost.3', 'Away_Possession lost.3', 'Home_Duels won.3', 'Away_Duels won.3', 'Home_Aerials won.3', 'Away_Aerials won.3', 'Home_Tackles.3', 'Away_Tackles.3', 'Home_Interceptions.3', 'Away_Interceptions.3', 'Home_Clearances.3', 'Away_Clearances.3', 'Home_Ball possession.3', 'Away_Ball possession.3', 'Home_Total shots.4', 'Away_Total shots.4', 'Home_Shots on target.4', 'Away_Shots on target.4', 'Home_Blocked shots.4', 'Away_Blocked shots.4', 'Home_Yellow cards.4', 'Away_Yellow cards.4', 'Home_Free kicks.4', 'Away_Free kicks.4', 'Home_Throw-ins.4', 'Away_Throw-ins.4', 'Home_Goal kicks.4', 'Away_Goal kicks.4', 'Home_Shots inside box.4', 'Away_Shots inside box.4', 'Home_Shots outside box.4', 'Away_Shots outside box.4', 'Home_Goalkeeper saves.4', 'Away_Goalkeeper saves.4', 'Home_Passes.4', 'Away_Passes.4', 'Home_Accurate passes.4', 'Away_Accurate passes.4', 'Home_Long balls.4', 'Away_Long balls.4', 'Home_Crosses.4', 'Away_Crosses.4', 'Home_Dribbles.4', 'Away_Dribbles.4', 'Home_Possession lost.4', 'Away_Possession lost.4', 'Home_Duels won.4', 'Away_Duels won.4', 'Home_Aerials won.4', 'Away_Aerials won.4', 'Home_Tackles.4', 'Away_Tackles.4', 'Home_Interceptions.4', 'Away_Interceptions.4', 'Home_Clearances.4', 'Away_Clearances.4', 'season.seasonCoverageInfo.editorCoverageLevel', 'Home_Corner kicks.3', 'Away_Corner kicks.3', 'Home_Offsides.3', 'Away_Offsides.3', 'Home_Ball possession.4', 'Away_Ball possession.4', 'Home_Offsides.4', 'Away_Offsides.4', 'Home_Shots off target.4', 'Away_Shots off target.4', 'Home_Corner kicks.4', 'Away_Corner kicks.4', 'Home_Hit woodwork.3', 'Away_Hit woodwork.3', 'homeTeam.ranking', 'awayTeam.ranking', 'lastPeriod', 'time.initial', 'time.max', 'time.extra', 'statusTime.prefix', 'statusTime.initial', 'statusTime.max', 'statusTime.timestamp', 'statusTime.extra', 'coverage','homeTeam.manager.name','awayTeam.manager.name','roundInfo.round']


    df.drop(additional_cols_to_drop, axis=1, inplace=True)

    # Convert Unix timestamps to datetime and create new features
    df['startTimestamp'] = pd.to_datetime(df['startTimestamp'], unit='s')
    df['year'] = df['startTimestamp'].dt.year
    df['month'] = df['startTimestamp'].dt.month
    df['day'] = df['startTimestamp'].dt.day
    df['hour'] = df['startTimestamp'].dt.hour
    df['minute'] = df['startTimestamp'].dt.minute
    df['day_of_week'] = df['startTimestamp'].dt.dayofweek
    df.drop('startTimestamp', axis=1, inplace=True)


    return df


def save_data(df, filename):
    df.to_csv(filename, index=False)

def get_column_types(df, target_var):
    # Separate numeric and categorical columns
    numeric_columns = [col for col in df.columns if df[col].dtype in ['int64', 'float64'] and col != target_var]
    categorical_columns = [col for col in df.columns if df[col].dtype == 'object' and col != target_var]

    return numeric_columns, categorical_columns




def save_encoded_data(data, filename):
    joblib.dump(data, filename)


def load_encoded_data(filename):
    return joblib.load(filename)



def print_column_info(df):
    # Create a dictionary to hold column info
    column_info = {}

    for column in df.columns:
        # Determine column type
        if df[column].dtype in ['int64', 'float64']:
            col_type = 'numeric'
        else:
            col_type = 'categorical'

        # Get the number of missing values in the column
        missing_values = df[column].isnull().sum()

        # Add info to the dictionary
        column_info[column] = (missing_values, col_type)

    # Sort the dictionary by the number of missing values (in descending order)
    sorted_column_info = dict(sorted(column_info.items(), key=lambda item: item[1][0], reverse=True))

    # Print the sorted column info
    for column, info in sorted_column_info.items():
        print(f'Column Name: {column}, Empty Values: {info[0]}, Type: {info[1]}')

def standardize_year(df, column_name='season.year'):
    # Function to convert year format
    def convert_year(year):
        if '/' in str(year):
            # Split and take the latter year
            year = '20' + str(year).split('/')[1]
        return year

    # Apply the function to the column
    df[column_name] = df[column_name].apply(convert_year)

    return df


def analyze_dataset(df):
    column_info = {}
    # Get column types
    numeric_columns, categorical_columns = get_column_types(df)
    print('Numeric columns:', numeric_columns)
    print('Categorical columns:', categorical_columns)
    # Loop through each column in the DataFrame
    for column in df.columns:
        column_data = df[column]

        # Check if column contains all missing values
        if column_data.isnull().all():
            column_info[column] = 'All values are missing.'
            continue

        # Check if column contains all the same value
        if column_data.nunique() == 1:
            column_info[column] = 'All values are the same.'
            continue

        # Get statistics for numeric columns
        if df[column].dtype in ['int64', 'float64']:
            column_info[column] = column_data.describe().to_dict()

        # Get unique values for categorical columns
        else:
            column_info[column] = {'Unique Values': column_data.unique().tolist()}

        # Add the number of unique values for each column
        column_info[column]['Number of Unique Values'] = column_data.nunique()

    # Print the results
    for column, info in column_info.items():
        print(f'Column Name: {column}\nInfo: {info}\n')


def fill_missing_values(df):
    # Fill the missing values with the mean value
    df['Home_Yellow cards'].fillna(0, inplace=True)
    df['Away_Yellow cards'].fillna(0, inplace=True)
    df['Home_Blocked shots'].fillna(df['Home_Blocked shots'].mean(), inplace=True)
    df['Away_Blocked shots'].fillna(df['Away_Blocked shots'].mean(), inplace=True)
    df['Home_Goalkeeper saves'].fillna(df['Home_Goalkeeper saves'].mean(), inplace=True)
    df['Away_Goalkeeper saves'].fillna(df['Away_Goalkeeper saves'].mean(), inplace=True)
    df['Home_Offsides'].fillna(0, inplace=True)
    df['Home_Shots on target'].fillna(df['Home_Shots on target'].mean(), inplace=True)
    df['Away_Shots on target'].fillna(df['Away_Shots on target'].mean(), inplace=True)
    df['Home_Shots off target'].fillna(df['Home_Shots off target'].mean(), inplace=True)
    df['Away_Shots off target'].fillna(df['Away_Shots off target'].mean(), inplace=True)
    df['homeScore.period2'].fillna(0, inplace=True)
    df['awayScore.period2'].fillna(0, inplace=True)
    df['Home_Total shots'].fillna(4, inplace=True)
    df['Away_Total shots'].fillna(5, inplace=True)
    df['Home_Corner kicks'].fillna(df['Home_Corner kicks'].mean(), inplace=True)
    df['Away_Corner kicks'].fillna(df['Away_Corner kicks'].mean(), inplace=True)
    df['homeScore.normaltime'].fillna(1, inplace=True)
    df['awayScore.normaltime'].fillna(1, inplace=True)
    df['Home_Goal kicks'].fillna(df['Home_Goal kicks'].mean(), inplace=True)
    df['Away_Goal kicks'].fillna(df['Away_Goal kicks'].mean(), inplace=True)
    df['Home_Free kicks'].fillna(df['Home_Free kicks'].mean(), inplace=True)
    df['Away_Free kicks'].fillna(df['Away_Free kicks'].mean(), inplace=True)
    df['Home_Fouls'].fillna(df['Home_Fouls'].mean(), inplace=True)
    df['Away_Fouls'].fillna(df['Away_Fouls'].mean(), inplace=True)
    return df

def clean_tournament_name(df):
    df['tournament.name'] = df['tournament.name'].str.replace(',', '')
    return df

def clean_data_season(df):
    # Your code to clean other data
    df['season.name'] = df['season.name'].apply(lambda x: re.sub(r'[\d/]+', '', x).strip())
    return df
def main():
    # Load your csv file
    df = load_data('Merged/merged_all.csv')

    df = standardize_year(df, column_name='season.year')

    # Clean tournament.name column
    df = clean_tournament_name(df)
    df = clean_data_season(df)
    df = clean_data(df)

    df = fill_missing_values(df)
    #print_column_info(df)
    #analyze_dataset(df)

    # Save the cleaned DataFrame to a new CSV file
    save_data(df, 'Merged/cleaned_merged_all.csv')


if __name__ == "__main__":
    main()
