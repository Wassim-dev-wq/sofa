import pandas as pd

def all_statistics_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/all_statistics_data_{id_value}.csv')
    # Drop the 'groupName' column
    df = df.drop('groupName', axis=1)
    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/all_statistics_data_{id_value}.csv', index=False)

def average_positions_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/average_positions_{id_value}.csv')
    # Drop the 'groupName' column
    df = df.drop('player_userCount', axis=1)
    df = df.drop('player_slug', axis=1)
    df = df.drop('player_firstName', axis=1)
    df = df.drop('player_lastName', axis=1)
    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/average_positions_{id_value}.csv', index=False)


def incidents_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/incidents_data_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'text', 'isLive', 'playerIn.firstName', 'playerIn.lastName',
        'playerIn.lastName', 'assist1.userCount', 'assist1.id',
        'player.slug', 'player.lastName', 'player.firstName',
        'player.id', 'playerIn.userCount', 'playerIn.id',
        'playerOut.firstName', 'playerOut.lastName', 'assist1.slug'
    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)

    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/incidents_data_{id_value}.csv', index=False)

def standings_cleaner(id_tournament, id_season):
    # Read the csv file
    df = pd.read_csv(f'Data/standings_data_{id_season}_{id_tournament}_total.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'descriptions', 'team.sport.slug', 'team.sport.name', 'team.slug',
        'team.shortName', 'promotion.id', 'team.teamColors.text',
        'team.teamColors.secondary', 'team.teamColors.primary', 'team.type',
        'team.disabled', 'id', 'team.id'
    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)

    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/standings_data_{id_season}_{id_tournament}_total.csv', index=False)

def lineups_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/game_lineups_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'player.firstName', 'player.lastName',
        'player.slug', 'player.marketValueCurrency',

    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)


    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/game_lineups_{id_value}.csv', index=False)

def event_data_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/event_data_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'customId', 'hasGlobalHighlights', 'hasEventPlayerStatistics', 'hasEventPlayerHeatMap',
        'detailId', 'crowdsourcingDataDisplayEnabled', 'id',
        'defaultPeriodCount', 'defaultPeriodLength', 'slug',
        'finalResultOnly', 'fanRatingEvent', 'seasonStatisticsType',
        'showTotoPromo' , 'tournament.slug' , 'tournament.category.slug' ,
        'tournament.category.sport.slug' , 'tournament.category.sport.id' , 'tournament.category.id',
        'tournament.uniqueTournament.slug', 'tournament.uniqueTournament.primaryColorHex', 'id',
        'tournament.uniqueTournament.secondaryColorHex', 'tournament.uniqueTournament.category.slug', 'tournament.uniqueTournament.category.sport.slug',
        'tournament.uniqueTournament.category.sport.id', 'tournament.uniqueTournament.category.id', 'tournament.uniqueTournament.category.flag',
        'tournament.uniqueTournament.userCount', 'awayTeam.teamColors.text', 'awayTeam.teamColors.secondary',
        'awayTeam.teamColors.primary', 'awayTeam.subTeams', 'changes.changes',
        'awayTeam.disabled', 'awayTeam.manager.slug', 'awayTeam.userCount',
        'awayTeam.teamColors.text', 'awayTeam.teamColors.secondary', 'awayTeam.teamColors.primary',
        'awayTeam.subTeams', 'awayTeam.manager.slug', 'awayTeam.userCount',
        'awayTeam.sport.id','awayTeam.sport.slug','awayTeam.sport.name',
        'awayTeam.slug','homeTeam.teamColors.text','homeTeam.teamColors.secondary',
        'tournament.category.sport.name','tournament.uniqueTournament.category.sport.name','tournament.uniqueTournament.id',
        'tournament.uniqueTournament.hasEventPlayerStatistics','tournament.uniqueTournament.crowdsourcingEnabled','tournament.uniqueTournament.hasPerformanceGraphFeature',
        'tournament.id','season.editor','season.id','status.code',

    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)

    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/event_data_{id_value}3.csv', index=False)

def past_games_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/past_games_data_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'customId', 'hasGlobalHighlights', 'id',
        'slug','finalResultOnly','tournament.slug',
        'tournament.category.slug','tournament.category.sport.slug',
        'tournament.category.sport.name','tournament.uniqueTournament.secondaryColorHex',
        'tournament.category.sport.id','tournament.category.id','tournament.uniqueTournament.slug',
        'tournament.uniqueTournament.primaryColorHex','id','id',
        'tournament.uniqueTournament.category.slug', 'tournament.uniqueTournament.category.sport.slug',
        'tournament.uniqueTournament.category.sport.id', 'tournament.uniqueTournament.category.id',
        'tournament.uniqueTournament.userCount', 'tournament.uniqueTournament.id',
        'tournament.uniqueTournament.hasEventPlayerStatistics', 'tournament.uniqueTournament.crowdsourcingEnabled',
        'tournament.uniqueTournament.hasPerformanceGraphFeature', 'tournament.priority',
        'tournament.uniqueTournament.displayInverseHomeAwayTeams', 'tournament.id',
        'status.code', 'homeTeam.slug',
        'homeTeam.sport.name', 'homeTeam.sport.slug',
        'homeTeam.disabled', 'homeTeam.type',
        'homeTeam.teamColors.primary', 'homeTeam.teamColors.secondary',
        'awayTeam.sport.name', 'awayTeam.sport.slug',
        'awayTeam.sport.id', 'awayTeam.disabled',
        'awayTeam.type', 'awayTeam.id',
        'awayTeam.subTeams', 'awayTeam.teamColors.primary',
        'awayTeam.teamColors.secondary', 'awayTeam.teamColors.text',
        'changes.changes', 'hasEventPlayerHeatMap',
        'hasEventPlayerStatistics', 'detailId',

    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)

    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/past_games_data_{id_value}.csv', index=False)


def event_h2h_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/event_h2h_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'customId', 'hasGlobalHighlights',
        'hasEventPlayerStatistics','hasEventPlayerHeatMap',
        'detailId','crowdsourcingDataDisplayEnabled',
        'slug','finalResultOnly',
        'tournament.slug','tournament.category.slug',
        'tournament.category.id','tournament.uniqueTournament.slug',
        'tournament.uniqueTournament.primaryColorHex','tournament.uniqueTournament.id',
        'tournament.uniqueTournament.hasEventPlayerStatistics','id',
        'tournament.uniqueTournament.crowdsourcingEnabled','tournament.uniqueTournament.hasPerformanceGraphFeature',
        'tournament.id','status.code',
        'status.description','status.type',
        'homeTeam.slug','homeTeam.sport.id',
        'homeTeam.sport.name','homeTeam.sport.slug',
        'homeTeam.disabled','homeTeam.type',
        'homeTeam.id','homeTeam.subTeams',
        'homeTeam.teamColors.primary','homeTeam.teamColors.secondary',
        'homeTeam.teamColors.text','awayTeam.slug',
        'awayTeam.sport.name','awayTeam.sport.slug',
        'awayTeam.disabled','awayTeam.type',
        'awayTeam.id','awayTeam.subTeams',
        'awayTeam.teamColors.primary','awayTeam.teamColors.secondary',
        'awayTeam.teamColors.text','changes.changes',
    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)

    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/event_h2h_{id_value}.csv', index=False)
