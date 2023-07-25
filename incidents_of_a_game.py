import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US, en;q=0.9",
}

response = requests.get('https://api.sofascore.com/api/v1/event/11327909/incidents', headers=headers)

if response.status_code == 200:
    try:
        data = response.json()

        # Normalize the 'incidents' data into a dataframe
        df = pd.json_normalize(data['incidents'])

        # Print the dataframe to inspect it
        print(df)

        # Save the dataframe to a CSV file
        df.to_csv('Data/incidents_data.csv', index=False)
    except ValueError:
        print("Unable to decode JSON response")
else:
    print("Failed to get data. HTTP status code: ", response.status_code)
