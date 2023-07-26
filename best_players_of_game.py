import requests
import pandas as pd

def fetch_and_save_best_players(id_value):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = requests.get(f'https://api.sofascore.com/api/v1/event/{id_value}/best-players', headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Normalize the 'bestHomeTeamPlayer' and 'bestAwayTeamPlayer' data into separate dataframes
            df_home = pd.json_normalize(data['bestHomeTeamPlayer'], sep='_')
            df_away = pd.json_normalize(data['bestAwayTeamPlayer'], sep='_')

            # Add prefix to distinguish between home and away player
            df_home = df_home.add_prefix('Home_')
            df_away = df_away.add_prefix('Away_')

            # Combine both dataframes
            df = pd.concat([df_home, df_away], axis=1)

            # Save the dataframe to a CSV file
            df.to_csv(f'Data/best_players_{id_value}.csv', index=False)
            print(f"[Best Players]Data for event ID {id_value} saved successfully.")

        except ValueError:
            print("Unable to decode JSON response")
    else:
        print("Failed to get data. HTTP status code: ", response.status_code)
