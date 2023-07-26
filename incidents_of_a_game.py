import requests
import pandas as pd

def fetch_and_save_incidents(id_value):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = requests.get(f'https://api.sofascore.com/api/v1/event/{id_value}/incidents', headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Normalize the 'incidents' data into a dataframe
            df = pd.json_normalize(data['incidents'])

            # Save the dataframe to a CSV file
            df.to_csv(f'Data/incidents_data_{id_value}.csv', index=False)
            print(f"[Incidents]Data for event ID {id_value} saved successfully.")

        except ValueError:
            print("Unable to decode JSON response")
    else:
        print("Failed to get data. HTTP status code: ", response.status_code)
