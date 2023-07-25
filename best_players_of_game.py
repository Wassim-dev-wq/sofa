import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US, en;q=0.9",
}

response = requests.get('https://api.sofascore.com/api/v1/event/11327909/best-players', headers=headers)

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

        # Print the dataframe to inspect it
        print(df)

        # Save the dataframe to a CSV file
        df.to_csv('Data/best_players_data.csv', index=False)
    except ValueError:
        print("Unable to decode JSON response")
else:
    print("Failed to get data. HTTP status code: ", response.status_code)
