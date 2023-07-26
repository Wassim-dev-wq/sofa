import requests
import pandas as pd

def fetch_and_save_standings(id_tournament,id_season):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    endpoints = ['total', 'home', 'away']
    for endpoint in endpoints:
        response = requests.get(f'https://api.sofascore.com/api/v1/tournament/{id_tournament}/season/{id_season}/standings/{endpoint}', headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()

                # Extract the first level of the nested structure
                df = pd.json_normalize(data, record_path=['standings', 'rows'])

                df.to_csv(f'Data/standings_data_{id_season}_{id_tournament}_{endpoint}.csv', index=False)
                print(f"[{endpoint.capitalize()} Standings] Data for event ID {id_season} saved successfully.")

            except ValueError:
                print("Unable to decode JSON response")
        else:
            print("Failed to get data. HTTP status code: ", response.status_code)

