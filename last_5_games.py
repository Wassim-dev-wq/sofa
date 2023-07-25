import requests
import pandas as pd
from pandas import json_normalize

# Define the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US, en;q=0.9",
    # Add other headers if needed
}

# Make the HTTP request with headers
response = requests.get('https://api.sofascore.com/api/v1/team/36246/events/last/0', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Try to get the JSON response body
        data = response.json()

        # Normalize the 'events' data from the JSON
        df = pd.json_normalize(data['events'])

        # Save the DataFrame to a CSV file
        df.to_csv('football_data.csv', index=False)
    except ValueError:
        print("Unable to decode JSON response")
else:
    print("Failed to get data. HTTP status code: ", response.status_code)
