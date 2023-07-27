import pandas as pd
import numpy as np

def all_statistics_data_cleaner(id_value):
    # Read the dataset
    df = pd.read_csv(f'Cleaned Data/all_statistics_data_{id_value}.csv')

    # Remove any duplicates
    df = df.drop_duplicates()

    # Function to clean the data
    # Function to clean the data
    # Function to clean the data
    def clean_data(value):
        if '%' in value and '(' not in value:  # '50%'
            return int(value.replace('%', ''))
        elif '(' in value and '/' not in value:  # '228 (64%)'
            return int(value.split(' ')[0])
        elif '(' in value and '/' in value:  # '22/74 (30%)'
            return int(value.split('(')[-1].replace('%)', ''))
        else:  # '355'
            return int(value)

    # Apply the function to the 'home' and 'away' columns
    df['home'] = df['home'].apply(lambda x: clean_data(x))
    df['away'] = df['away'].apply(lambda x: clean_data(x))

    # Rename the columns
    df.columns = ['Statistic', 'Home Team', 'Away Team']

    # Resetting index to 'statistic'
    df.set_index('Statistic', inplace=True)

    # Flatten the dataframe into a single row
    single_row = df.T.values.flatten()

    # Create new dataframe with single row
    df_single_row = pd.DataFrame(single_row).T

    # Creating new meaningful column names
    new_columns = [f"{team}_{stat}" for stat in df.index for team in ['Home', 'Away']]

    # Assign the new column names to the single row dataframe
    df_single_row.columns = new_columns

    # Save the new dataframe to a CSV file
    df_single_row.to_csv(f'Transformed/all_statistics_data_{id_value}.csv', index=False)

all_statistics_data_cleaner(10833986)