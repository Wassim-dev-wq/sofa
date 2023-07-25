import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US, en;q=0.9",
}

response = requests.get('https://api.sofascore.com/api/v1/event/11327909', headers=headers)

if response.status_code == 200:
    try:
        data = response.json()

        # Create an empty DataFrame to store all the data
        all_data_df = pd.json_normalize(data['event'], max_level=1)

        # Print the dataframe to inspect it
        print(all_data_df)

        # Save the dataframe to a CSV file
        all_data_df.to_csv('Data/event_data.csv', index=False)

    except ValueError:
        print("Unable to decode JSON response")
else:
    print("Failed to get data. HTTP status code: ", response.status_code)
