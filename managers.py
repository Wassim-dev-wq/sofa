import requests
import pandas as pd

def fetch_and_save_game_managers(id_value):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = requests.get(f'https://api.sofascore.com/api/v1/event/{id_value}/managers', headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Create DataFrame directly from the home and away manager dictionaries
            home_manager = pd.DataFrame([data['homeManager']], index=['home'])
            away_manager = pd.DataFrame([data['awayManager']], index=['away'])

            # Concatenate the home and away manager dataframes
            df = pd.concat([home_manager, away_manager])

            # Save the DataFrame to a CSV file
            df.to_csv(f'Data/game_managers_{id_value}.csv')

            print(f"[Managers]Data for event ID {id_value} saved successfully.")
        except ValueError:
            print("Unable to decode JSON response")
    else:
        print("Failed to get data. HTTP status code: ", response.status_code)
