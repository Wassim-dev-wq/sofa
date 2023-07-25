import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US, en;q=0.9",
}

response = requests.get('https://api.sofascore.com/api/v1/team/2829/unique-tournament/8/season/42409/top-players/overall', headers=headers)

if response.status_code == 200:
    try:
        data = response.json()

        # Create an empty DataFrame to store all the data
        all_data_df = pd.DataFrame()

        # For each category in the 'topPlayers' object
        for category in data['topPlayers'].keys():
            # Normalize the data into a dataframe
            df_category = pd.json_normalize(data['topPlayers'][category])

            # Add a new column to the dataframe to store the category
            df_category['category'] = category

            # Append the df_category DataFrame to the all_data_df DataFrame
            all_data_df = all_data_df._append(df_category, ignore_index=True)

        # Print the dataframe to inspect it
        print(all_data_df)

        # Save the dataframe to a CSV file
        all_data_df.to_csv('Data/top_players_data.csv', index=False)

    except ValueError:
        print("Unable to decode JSON response")
else:
    print("Failed to get data. HTTP status code: ", response.status_code)
