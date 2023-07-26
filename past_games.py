import requests
import pandas as pd


def fetch_and_save_past_games(id_value):
    # Define the headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
        # Add other headers if needed
    }

    # Make the HTTP request with headers
    response = requests.get(f'https://api.sofascore.com/api/v1/team/{id_value}/events/last/0', headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Try to get the JSON response body
            data = response.json()

            # Normalize the 'events' data from the JSON
            df = pd.json_normalize(data['events'])

            # Save the DataFrame to a CSV file
            df.to_csv(f'Data/past_games_data_{id_value}.csv', index=False)

            print(f"[Past Games]Data for event ID {id_value} saved successfully.")
        except ValueError:
            print("Unable to decode JSON response")
    else:
        print("Failed to get data. HTTP status code: ", response.status_code)
