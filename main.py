import pandas as pd

# Load the data from the csv files into pandas DataFrames
df_odds = pd.read_csv('odds.csv')
df_football = pd.read_csv('football_data.csv')

# Merge the dataframes on the 'id' column
df_merged = pd.merge(df_football, df_odds, on='id', how='inner')

# Write the merged dataframe to a new csv file
df_merged.to_csv('merged_data.csv', index=False)
