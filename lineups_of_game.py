import requests
import pandas as pd
from pandas import json_normalize


def fetch_and_save_lineups(id_value):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = requests.get(f'https://api.sofascore.com/api/v1/event/{id_value}/lineups', headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Create empty list to hold dataframes
            dfs = []

            # Iterate over home and away
            for team in ['home', 'away']:
                # Extract players list into a dataframe
                players_df = json_normalize(data[team]['players'])

                # Add team and player type columns
                players_df['team'] = team
                players_df['player_type'] = players_df['substitute'].apply(lambda x: 'substitute' if x else 'main')

                # Append to list of dataframes
                dfs.append(players_df)

            # Concatenate all dataframes
            final_df = pd.concat(dfs, ignore_index=True)


            # Save the dataframe to a CSV file
            final_df.to_csv(f'Data/game_lineups_{id_value}.csv', index=False)
            print(f"[Lineups]Data for event ID {id_value} saved successfully.")

        except ValueError:
            print("Unable to decode JSON response")
    else:
        print("Failed to get data. HTTP status code: ", response.status_code)
