import requests
import pandas as pd

def fetch_and_save_statistics(id_value):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US, en;q=0.9",
    }

    response = requests.get(f'https://api.sofascore.com/api/v1/event/{id_value}/statistics', headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            # Create an empty DataFrame to store all statistics
            all_stats_df = pd.DataFrame()

            # Flatten the statistics data
            for stat_group in data['statistics']:
                df = pd.json_normalize(stat_group['groups'])

                for idx, row in df.iterrows():
                    df_items = pd.json_normalize(row['statisticsItems'])
                    df_items['groupName'] = row['groupName']

                    # Append the df_items DataFrame to the all_stats_df DataFrame
                    all_stats_df = all_stats_df._append(df_items)

            # Save the DataFrame to a CSV file
            all_stats_df.to_csv(f'Data/all_statistics_data_{id_value}.csv', index=False)
            print(f"[Statistics]Data for event ID {id_value} saved successfully.")

        except ValueError:
            print("Unable to decode JSON response")
    else:
        print("Failed to get data. HTTP status code: ", response.status_code)
