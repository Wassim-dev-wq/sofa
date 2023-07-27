import pandas as pd
import numpy as np
import os

def get_max_length(files):
    max_length = 0
    for file in files:
        if os.path.isfile(file):
            df = pd.read_csv(file)
            length = len(df)
            max_length = max(max_length, length)
    return max_length

def duplicate_data_to_length(df, max_length):
    while len(df) < max_length:
        df = pd.concat([df, df], ignore_index=True)
    return df[:max_length]

def merge_data(match_id, id_tournament, id_season, id_value_hometeam, id_value_awayteam, id_value_h2h,date):
    files = [
        f'Cleaned Data/event_data_{match_id}.csv',
        f'Cleaned Data/all_statistics_data_{match_id}.csv',
        #f'Cleaned Data/standings_data_{id_season}_{id_tournament}_total.csv',
        f'Cleaned Data/event_h2h_{id_value_h2h}.csv',
        f'Cleaned Data/past_games_data_{id_value_hometeam}.csv',
        f'Cleaned Data/past_games_data_{id_value_awayteam}.csv',
        f'Cleaned Data/game_lineups_{match_id}.csv',
    ]

    max_length = get_max_length(files)

    dataframes = []
    for file in files:
        try:
            df = pd.read_csv(file)
            df = duplicate_data_to_length(df, max_length)
            dataframes.append(df)
        except FileNotFoundError:
            print(f"File {file} not found.")

    df_merged = pd.concat(dataframes, axis=1)
    # insert 'match_id' at the first column (index 0)
    df_merged.insert(0, 'match_id', match_id)

    df_merged.to_csv(f'Merged/merged_data_{match_id}.csv', index=False)



def merge_data_statistics(match_id, id_tournament, id_season, id_value_hometeam, id_value_awayteam, id_value_h2h,date):
    files = [
        f'Data/event_data_{match_id}.csv',
        f'Data/all_statistics_data_{match_id}.csv'
    ]

    max_length = get_max_length(files)

    dataframes = []
    for file in files:
        try:
            df = pd.read_csv(file)
            df['match_id'] = match_id
            df = duplicate_data_to_length(df, max_length)
            dataframes.append(df)
        except FileNotFoundError:
            print(f"File {file} not found.")

    df_merged = pd.concat(dataframes, axis=1)

    df_merged.to_csv(f'Merged/merged_data_{match_id}.csv', index=False)