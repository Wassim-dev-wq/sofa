import os

import pandas as pd

from data_processing import merge_data_statistics


def merge_all_cleaned_data():
    path = 'Merged/'
    files = [file for file in os.listdir(path) if file.endswith('.csv')]

    df_list = []
    for file in files:
        df = pd.read_csv(path + file, low_memory=False)
        df_list.append(df)

    merged_df = pd.concat(df_list, ignore_index=True)
    merged_df.to_csv('Merged/merged_all.csv', index=False)

    '''
    df_odds = pd.read_csv('Data/odds.csv')
    df_merged = pd.merge(merged_df, df_odds, left_on='match_id', right_on='id', how='inner')
    df_merged.to_csv(f'Merged/Cleaned/merged_all.csv', index=False)
    '''

def merge_all_data_cleaner():
    # Read the csv file
    df = pd.read_csv('Merged/merged_all.csv')
    columns_to_drop = ['hasBet365LiveStream', 'bet365ExcludedCountryCodes',
                       'tournament.category.flag', 'venue.id',
                       'homeTeam.foundationDateTimestamp', 'Home_Hit woodwork.2',
                       'Away_Hit woodwork.2', 'aggregatedWinnerCode',
                       'previousLegEventId', 'cupMatchesInRound',
                       'roundInfo.name', 'roundInfo.slug'
                       'roundInfo.cupRoundType', 'awayScore.aggregated'
                       'coverage'
    ]
    # Drop the columns
    for col in columns_to_drop:
        try:
            df = df.drop(col, axis=1)
        except KeyError:
            pass  # do nothing if the column is not in the dataframe
    # Write the dataframe back to the csv
    df.to_csv('Merged/merged_all.csv', index=False)
#merge_all_data_cleaner()
#merge_all_cleaned_data()