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
    merged_df.to_csv('Merged/Cleaned/merged_all.csv', index=False)

    '''
    df_odds = pd.read_csv('Data/odds.csv')
    df_merged = pd.merge(merged_df, df_odds, left_on='match_id', right_on='id', how='inner')
    df_merged.to_csv(f'Merged/Cleaned/merged_all.csv', index=False)
    '''

