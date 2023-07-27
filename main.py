import os
from datetime import timedelta, datetime

import pandas as pd
from all_day_games import fetch_all_games
from best_players_of_game import fetch_and_save_best_players
from data_cleaner import all_statistics_cleaner, average_positions_cleaner, incidents_cleaner, standings_cleaner, \
    lineups_cleaner, event_data_cleaner, past_games_cleaner, event_h2h_cleaner, all_data_cleaner, merged_data_cleaner
from data_processing import merge_data, merge_data_statistics
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

# Define lock
lock = threading.Lock()

date_start = "2023-07-20"
date_end = "2023-07-21"

# Define date range function
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def thread_task(event_id):
    try:
        with lock:
            event_id = id_list[i]
            fetch_and_save_statistics(event_id)
            fetch_and_save_incidents(event_id)
            fetch_and_save_best_players(event_id)
            fetch_and_save_lineups(event_id)
            id_season, id_tournament, id_value_h2h, id_value_hometeam, id_value_awayteam = fetch_and_save_game_data(event_id)
            fetch_and_save_standings(id_tournament, id_season)
            fetch_and_save_event_h2h(id_value_h2h)
            fetch_and_save_past_games(id_value_hometeam)
            fetch_and_save_past_games(id_value_awayteam)
            fetch_and_save_game_managers(event_id)
            fetch_and_save_average_positions_game(event_id)

            # Call cleaner functions
            all_statistics_cleaner(event_id)
            average_positions_cleaner(event_id)
            lineups_cleaner(event_id)
            event_data_cleaner(event_id)
            past_games_cleaner(id_value_hometeam)
            past_games_cleaner(id_value_awayteam)
            event_h2h_cleaner(id_value_h2h)
            #incidents_cleaner(event_id)
            #standings_cleaner(id_tournament, id_season)

            #merge_data_statistics(event_id, id_tournament, id_season, id_value_hometeam, id_value_awayteam, id_value_h2h,date)

            merge_data(event_id, id_tournament, id_season, id_value_hometeam, id_value_awayteam, id_value_h2h,date)
            merged_data_cleaner(event_id)
            #all_data_cleaner(event_id)
    except Exception as e:
        print(f"An error occurred: {e}")





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
    threads = []
    for i in range(1):
        event_id = id_list[i]
        thread = threading.Thread(target=thread_task, args=(event_id,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()



