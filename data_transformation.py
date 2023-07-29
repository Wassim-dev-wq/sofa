import pandas as pd
import numpy as np

def all_statistics_data_cleaner(id_value):
    # Read the dataset
    df = pd.read_csv(f'Cleaned Data/all_statistics_data_{id_value}.csv')

    # Remove any duplicates
    df = df.drop_duplicates()

    # Function to clean the data
    def clean_data(value):
        try:
            if '%' in value and '(' not in value:  # '50%'
                return int(value.replace('%', ''))
            elif '(' in value and '/' not in value:  # '228 (64%)'
                return int(value.split(' ')[0])
            elif '(' in value and '/' in value:  # '22/74 (30%)'
                return int(value.split('(')[-1].replace('%)', ''))
            else:  # '355'
                return int(value)
        except Exception as e:
            print(f'Error encountered: {e}. Skipping column...')
            return None

    # Apply the function to the 'home' and 'away' columns
    for column in ['home', 'away']:
        if column in df.columns:
            df[column] = df[column].apply(lambda x: clean_data(x))

    # Drop any columns that were not successfully cleaned
    df = df.dropna(axis=1)

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



def data_statistics_event_combine(id_value):
    # Read the csv files
    df = pd.read_csv(f'Transformed/all_statistics_data_{id_value}.csv')
    df_event = pd.read_csv(f'Cleaned Data/event_data_{id_value}.csv')

    # Concatenate the dataframes along the column axis
    df_combined = pd.concat([df_event, df], axis=1)

    # Add 'match_id' column to the combined dataframe and make it the first column
    df_combined.insert(0, 'match_id', id_value)

    # Save the combined dataframe to a csv file
    df_combined.to_csv(f'Merged/merged_data_{id_value}.csv', index=False)
