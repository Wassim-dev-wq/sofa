import requests
import pandas as pd

# Function to convert fractional odds to decimal
def fractional_to_decimal(fractional_odds):
    fractional_odds = fractional_odds.split('/')
    decimal_odds = int(fractional_odds[0]) / int(fractional_odds[1]) + 1
    return round(decimal_odds, 2)  # round to 2 decimal places

# Define the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US, en;q=0.9",
    # Add other headers if needed
}

# Make the HTTP request with headers
response = requests.get('https://api.sofascore.com/api/v1/sport/football/odds/1/2023-07-24', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Try to get the JSON response body
        data = response.json()

        # Create an empty DataFrame
        df = pd.DataFrame()

        # Extract the required data and add it to the DataFrame
        for key in data['odds']:
            id_ = key  # Use the key of the dictionary as the 'id'
            choices = data['odds'][key]['choices']

            choice_dict = {'id': id_}  # Create a dictionary to hold choices

            # Loop through the choices and convert each to decimal odds
            for choice in choices:
                decimal_odds = fractional_to_decimal(choice['fractionalValue'])
                # Add the choice to the choice_dict with the name of choice as key
                choice_dict['choice_' + choice['name']] = decimal_odds

            # Append the row to the DataFrame
            df = df._append(choice_dict, ignore_index=True)

        # Save the DataFrame to a CSV file
        df.to_csv('odds.csv', index=False)

    except ValueError:
        print("Unable to decode JSON response")
else:
    print("Failed to get data. HTTP status code: ", response.status_code)
