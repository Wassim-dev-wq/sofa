import pandas as pd
import requests


def fetch_and_save_game_data(id_value):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }
    print(id_value)
    url = f'https://api.sofascore.com/api/v1/event/{id_value}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Flatten the JSON data and create a DataFrame
            all_data_df = pd.json_normalize(data['event'], max_level=6)

            # Get the 'season.id' and 'tournament.id' values
            id_season = all_data_df.loc[0, 'season.id']
            id_tournament = all_data_df.loc[0, 'tournament.id']
            id_value_h2h = all_data_df.loc[0, 'customId']
            id_value_hometeam = all_data_df.loc[0, 'homeTeam.id']
            id_value_awayteam = all_data_df.loc[0, 'awayTeam.id']

            # Save the DataFrame to a CSV file
            all_data_df.to_csv(f'Data/event_data_{id_value}.csv', index=False)

            print(f"[Event]Data for event ID {id_value} saved successfully.")

            # Return the 'season.id' and 'tournament.id' values
            return id_season, id_tournament, id_value_h2h, id_value_hometeam, id_value_awayteam

        except ValueError:
            print("Unable to decode JSON response")
    else:
        print(f"Failed to get data. HTTP status code: {response.status_code}")
