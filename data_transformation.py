import numpy as np
import pandas as pd


# Function to clean percentages
def clean_percentage(val):
    try:
        return float(val.strip('%')) / 100
    except:
        return None


# Function to clean ratios
def clean_ratio(val):
    try:
        num, denom = val.split('/')
        return float(num) / float(denom)
    except:
        return None


# Function to clean count data
def clean_count(val):
    try:
        return float(val)
    except:
        return None


def all_statistics_transformer(id_value):
    # Read CSV files
    df_statistics = pd.read_csv(f'Cleaned Data/all_statistics_data_{id_value}.csv')

    # insert 'match_id' at the first column (index 0)
    #df_statistics.insert(0, 'match_id', 10833986)

    # define the stats columns
    stats_cols = ['name', 'home', 'away']

    # make sure all rows have exactly 3 columns
    df = df_statistics.dropna(subset=stats_cols)

    # Count the number of stats for each match
    stats_per_match = df_statistics[df_statistics['name'] == 'Ball possession'].shape[0]

    # reshape the data
    match_ids = np.repeat(np.arange(len(df) // stats_per_match), stats_per_match)
    df['match_id'] = match_ids

    # pivot the table
    df_pivot = df.pivot(index='match_id', columns='name')

    # flatten MultiIndex columns
    df_pivot.columns = ['_'.join(col).rstrip('_') for col in df_pivot.columns.values]

    # reset index
    df_clean = df_pivot.reset_index(drop=True)

    # handle erroneous data (replace non-numeric values with NaN)
    for col in df_clean.columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # fill missing values
    df_clean = df_clean.fillna(df_clean.median())

    # save to csv
    df_clean.to_csv('clean_match_data.csv', index=False)


all_statistics_transformer(10833986)
