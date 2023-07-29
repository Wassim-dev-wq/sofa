import os
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta, datetime

import pandas as pd
from all_day_games import fetch_all_games
from best_players_of_game import fetch_and_save_best_players
from data_cleaner import all_statistics_cleaner, average_positions_cleaner, incidents_cleaner, standings_cleaner, \
    lineups_cleaner, event_data_cleaner, past_games_cleaner, event_h2h_cleaner, all_data_cleaner, merged_data_cleaner
from data_processing import merge_data, merge_data_statistics
from data_transformation import all_statistics_data_cleaner, data_statistics_event_combine
from game_average_positions import fetch_and_save_average_positions_game
from game_data import fetch_and_save_game_data
from game_h2h_data import fetch_and_save_event_h2h
from lineups_of_game import fetch_and_save_lineups
from managers import fetch_and_save_game_managers
from odds import fetch_odds
from game_statistics import fetch_and_save_statistics
from incidents_of_a_game import fetch_and_save_incidents
from past_games import fetch_and_save_past_games
from standing_of_team import fetch_and_save_standings
import threading


# Define date range function
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def thread_task(event_id):
    try:
        id_season, id_tournament, id_value_h2h, id_value_hometeam, id_value_awayteam = fetch_and_save_game_data(event_id)
        fetch_and_save_statistics(event_id)
        event_data_cleaner(event_id)
        all_statistics_cleaner(event_id)
        all_statistics_data_cleaner(event_id)
        data_statistics_event_combine(event_id)
    except Exception as e:
        print(f'Error encountered: {e}.')


date_start = '2023-04-01'
date_end = '2023-06-29'
# Convert strings to dates
start_date = datetime.strptime(date_start, "%Y-%m-%d")
end_date = datetime.strptime(date_end, "%Y-%m-%d")

# Loop through each date in range>
for single_date in daterange(start_date, end_date):
    date = single_date.strftime("%Y-%m-%d")
    # Call the functions to fetch all games and odds
    fetch_all_games(date)
    fetch_odds(date)

    df_odds = pd.read_csv('Data/odds.csv')
    df_football = pd.read_csv('Data/football_data.csv')
    df_merged = pd.merge(df_football, df_odds, on='id', how='inner')
    df_merged.to_csv(f'Data/merged_data_{date}.csv', index=False)
    ids = df_football['id']
    id_list = ids.to_list()
    print(id_list)

    # Define the maximum number of threads
    max_threads = 100

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Use map to execute the function for each item in id_list
        executor.map(thread_task, id_list)



