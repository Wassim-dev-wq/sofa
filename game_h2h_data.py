import requests
import pandas as pd
from pandas import json_normalize

def fetch_and_save_event_h2h(id_value_h2h):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = requests.get(f'https://api.sofascore.com/api/v1/event/{id_value_h2h}/h2h/events', headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Flatten the JSON data and create a DataFrame
            events_df = json_normalize(data, 'events', max_level=2)

            # Save the DataFrame to a CSV file
            events_df.to_csv(f'Data/event_h2h_{id_value_h2h}.csv', index=False)
            print(f"[H2H Events] Data for event ID {id_value_h2h} saved successfully.")

        except ValueError:
            print("Unable to decode JSON response")
    else:
        print(f"Failed to get data. HTTP status code: {response.status_code}")
