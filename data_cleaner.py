import pandas as pd


def all_statistics_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/all_statistics_data_{id_value}.csv')
    # Drop the 'groupName' column
    df = df.drop('groupName', axis=1)
    df = df.drop('compareCode', axis=1)
    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/all_statistics_data_{id_value}.csv', index=False)

def average_positions_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Data/average_positions_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'player_userCount', 'player_slug',
        'player_firstName', 'player_lastName',
        'pointsCount', 'player_id'
    ]

    # Drop the columns
    df = df.drop(columns_to_drop, axis=1)
    # Write the dataframe back to the csv
    df.to_csv(f'Cleaned Data/average_positions_{id_value}.csv', index=False)

all_statistics_cleaner(10833993)
average_positions_cleaner(10833993)
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


def all_data_cleaner(id_value):
    # Read the csv file
    df = pd.read_csv(f'Merged/merged_data_{id_value}.csv')

    # List of columns to be dropped
    columns_to_drop = [
        'customId', 'slug', 'tournament.name', 'tournament.slug', 'tournament.category.name',
       'tournament.category.slug', 'tournament.category.flag',
       'tournament.uniqueTournament.name',
       'tournament.uniqueTournament.slug', 'tournament.uniqueTournament.primaryColorHex',
       'tournament.uniqueTournament.secondaryColorHex',
       'tournament.uniqueTournament.category.flag',
       'tournament.uniqueTournament.category.slug', 'homeTeam.slug', 'homeTeam.nameCode',
       'homeTeam.manager.slug', 'homeTeam.manager.shortName',
       'homeTeam.manager.country.alpha2',
       'homeTeam.manager.country.name', 'homeTeam.teamColors.primary',
       'homeTeam.teamColors.secondary', 'homeTeam.teamColors.text', 'homeTeam.name',
       'awayTeam.name',
       'awayTeam.slug', 'awayTeam.manager.name', 'awayTeam.manager.slug',
       'awayTeam.manager.shortName', 'awayTeam.manager.country.alpha2',
       'awayTeam.manager.country.name',
       'awayTeam.nameCode', 'awayTeam.teamColors.primary', 'awayTeam.teamColors.secondary',
       'awayTeam.teamColors.text', 'status.description', 'venue.city.name',
       'venue.stadium.name',
       'referee.name', 'referee.slug', 'referee.country.alpha2', 'referee.country.name',
       'referee.sport.name', 'referee.sport.slug', 'roundInfo.name', 'roundInfo.slug',
       'team.name', 'team.slug', 'team.shortName', 'team.teamColors.primary',
       'team.teamColors.secondary', 'team.teamColors.text', 'promotion.text',
       'startTimestamp',
       'tournament.category.sport.slug', 'tournament.uniqueTournament.category.sport.slug',
       'homeTeam.sport.slug', 'awayTeam.sport.slug', 'team.sport.slug',
       'tournament.uniqueTournament.category.name',
       'tournament.uniqueTournament.category.sport.name',
        'hasGlobalHighlights','hasEventPlayerStatistics',
        'hasEventPlayerHeatMap','detailId',
        'crowdsourcingDataDisplayEnabled','id',
        'finalResultOnly','seasonStatisticsType',
        'showTotoPromo','tournament.category.sport.name',
        'tournament.category.sport.id','tournament.uniqueTournament.category.sport.id',
        'tournament.uniqueTournament.hasEventPlayerStatistics','tournament.uniqueTournament.crowdsourcingEnabled',
        'tournament.uniqueTournament.hasPerformanceGraphFeature','tournament.uniqueTournament.displayInverseHomeAwayTeams',
        'season.editor','status.code',
        'status.type','homeTeam.sport.name',
        'homeTeam.sport.id','homeTeam.disabled',
        'slug.1', 'slug.2', 'slug.3',
        'customId.1', 'customId.2', 'customId.3',
        'id.1', 'id.2', 'id.3', 'id.4',
        'tournament.uniqueTournament.id.1', 'tournament.uniqueTournament.id.2', 'tournament.uniqueTournament.id.3',
        'tournament.id.1', 'tournament.id.2', 'tournament.id.3',
        'tournament.category.id.1', 'tournament.category.id.2', 'tournament.category.id.3',
        'homeTeam.id.1', 'homeTeam.id.2', 'homeTeam.id.3',
        'awayTeam.id.1', 'awayTeam.id.2', 'awayTeam.id.3',
        'team.id',
        'homeTeam.manager.id',
        'awayTeam.manager.id',
        'referee.id',
        'venue.id',
        'season.id',
        'winnerCode.1', 'winnerCode.2', 'winnerCode.3',
        'tournament.priority.1', 'tournament.priority.2', 'tournament.priority.3',
        'team.sport.id', 'homeTeam.sport.id', 'awayTeam.sport.id',
        'homeTeam.sport.id.1', 'homeTeam.sport.id.2', 'homeTeam.sport.id.3',
        'awayTeam.sport.id.1', 'awayTeam.sport.id.2', 'awayTeam.sport.id.3',
        'tournament.category.sport.id.1', 'tournament.category.sport.id.2',
        'tournament.uniqueTournament.category.sport.id.1', 'tournament.uniqueTournament.category.sport.id.2',
        'changes.changeTimestamp', 'changes.changeTimestamp.1', 'changes.changeTimestamp.2', 'changes.changeTimestamp.3',
        'slug', 'customId', 'tournament.id', 'homeTeam.id', 'awayTeam.id', 'currentPeriodStartTimestamp',
        'startTimestamp.1', 'startTimestamp.2', 'startTimestamp.3', 'homeTeam.country.alpha2',
        'awayTeam.country.alpha2', 'homeTeam.sport.name', 'awayTeam.sport.name', 'team.sport.name',
        'tournament.uniqueTournament.primaryColorHex.1', 'tournament.uniqueTournament.secondaryColorHex.1',
        'tournament.uniqueTournament.primaryColorHex.2', 'tournament.uniqueTournament.secondaryColorHex.2',
        'tournament.uniqueTournament.primaryColorHex.3', 'tournament.uniqueTournament.secondaryColorHex.3',
        'tournament.name.1', 'tournament.name.2', 'tournament.name.3', 'homeTeam.name.1', 'homeTeam.name.2',
        'homeTeam.name.3', 'awayTeam.name.1', 'awayTeam.name.2', 'awayTeam.name.3', 'homeTeam.country.alpha2.1',
        'homeTeam.country.alpha2.2', 'awayTeam.country.alpha2.1', 'awayTeam.country.alpha2.2', 'homeTeam.sport.name.1',
        'homeTeam.sport.name.2', 'homeTeam.sport.name.3', 'awayTeam.sport.name.1', 'awayTeam.sport.name.2',
        'awayTeam.sport.name.3', 'tournament.category.sport.name.1', 'tournament.category.sport.name.2',
        'slug', 'customId', 'detailId.1', 'detailId.2', 'detailId.3',
        'coverage', 'coverage.1', 'coverage.2', 'compareCode', 'groupName', 'isAwarded',
        'tournament.category.sport', 'tournament.category.flag.1', 'tournament.uniqueTournament.name.1',
        'tournament.uniqueTournament.slug.1', 'tournament.uniqueTournament.category',
        'tournament.uniqueTournament.hasEventPlayerStatistics.1',
        'tournament.uniqueTournament.crowdsourcingEnabled.1',
        'tournament.uniqueTournament.hasPerformanceGraphFeature.1',
        'tournament.uniqueTournament.displayInverseHomeAwayTeams.1', 'status.code.1', 'status.description.1',
        'status.type.1', 'homeTeam.slug.1', 'homeTeam.shortName.1', 'homeTeam.sport.slug.1',
        'homeTeam.nameCode.1', 'homeTeam.teamColors.primary.1', 'homeTeam.teamColors.secondary.1',
        'homeTeam.teamColors.text.1', 'awayTeam.slug.1', 'awayTeam.shortName.1', 'awayTeam.sport.slug.1',
        'awayTeam.nameCode.1', 'awayTeam.teamColors.primary.1', 'awayTeam.teamColors.secondary.1',
        'awayTeam.teamColors.text.1', 'changes.changes', 'changes.changes.1', 'changes.changes.2',
        'changes.changes.3', 'homeScore.display', 'homeScore.display.1', 'homeScore.display.2',
        'homeScore.display.3', 'awayScore.display', 'awayScore.display.1', 'awayScore.display.2',
        'awayScore.display.3', 'roundInfo.name.1', 'roundInfo.slug.1', 'roundInfo.cupRoundType',
        'homeScore.period1.1', 'homeScore.period2.1', 'homeScore.normaltime.1', 'homeScore.period1.2',
        'homeScore.period2.2', 'homeScore.normaltime.2', 'homeScore.period1.3', 'homeScore.period2.3',
        'homeScore.normaltime.3', 'awayScore.period1.1', 'awayScore.period2.1', 'awayScore.normaltime.1',
        'awayScore.period1.2', 'awayScore.period2.2', 'awayScore.normaltime.2', 'awayScore.period1.3',
        'awayScore.period2.3', 'awayScore.normaltime.3', 'homeScore.extra1', 'homeScore.extra2',
        'homeScore.overtime', 'awayScore.extra1', 'awayScore.extra2', 'awayScore.overtime',
        'homeTeam.userCount.1', 'homeTeam.userCount.2', 'homeTeam.userCount.3', 'awayTeam.userCount.1',
        'awayTeam.userCount.2', 'awayTeam.userCount.3', 'homeScore.current.1', 'homeScore.current.2',
        'homeScore.current.3', 'awayScore.current.1', 'awayScore.current.2', 'awayScore.current.3',
        'time.injuryTime1.2', 'time.injuryTime2.2', 'time.currentPeriodStartTimestamp.2',
        'time.injuryTime1.3', 'time.injuryTime2.3', 'time.currentPeriodStartTimestamp.3',
        'time.injuryTime3', 'time.injuryTime4', 'homeScore.penalties', 'awayScore.penalties',
        'homeScore.penalties.1', 'awayScore.penalties.1', 'hasEventPlayerStatistics.1',
        'hasEventPlayerHeatMap.1', 'hasEventPlayerStatistics.2', 'hasEventPlayerHeatMap.2',
        'hasEventPlayerStatistics.3', 'hasEventPlayerHeatMap.3', 'crowdsourcingDataDisplayEnabled.1',
        'finalResultOnly.1', 'crowdsourcingDataDisplayEnabled.2', 'finalResultOnly.2',
        'crowdsourcingDataDisplayEnabled.3', 'finalResultOnly.3',
        'homeTeam.teamColors.primary.3','homeTeam.subTeams.3',
        'homeTeam.teamColors.text.3','homeTeam.teamColors.secondary.3',
        'awayTeam.sport.slug.3','awayTeam.disabled.3',
        'awayTeam.type.3','awayTeam.subTeams.3',
        'awayTeam.teamColors.primary.3','awayTeam.teamColors.secondary.3',
        'awayTeam.teamColors.text.3','homeTeam.disabled.3',
        'homeTeam.sport.slug.3','status.code.3',
        'tournament.uniqueTournament.displayInverseHomeAwayTeams.3','tournament.uniqueTournament.hasPerformanceGraphFeature.3',
        'tournament.uniqueTournament.crowdsourcingEnabled.3','tournament.uniqueTournament.hasEventPlayerStatistics.3',
        'tournament.uniqueTournament.category.sport.slug.2','tournament.uniqueTournament.category.sport.name.2',
        'tournament.category.sport.slug.2','hasGlobalHighlights.3',
        'awayTeam.teamColors.text.2','awayTeam.teamColors.secondary.2',
        'awayTeam.teamColors.primary.2','awayTeam.subTeams.2',
        'awayTeam.disabled.2','awayTeam.sport.slug.2',
        'homeTeam.teamColors.text.2','homeTeam.teamColors.secondary.2',
        'homeTeam.teamColors.primary.2','homeTeam.subTeams.2',
        'homeTeam.type.2','homeTeam.disabled.2',
        'homeTeam.sport.slug.2','status.type.2',
        'tournament.uniqueTournament.category.sport.slug.1','tournament.uniqueTournament.category.slug.1',
        'tournament.category.sport.slug.1','awayTeam.subTeams.1',
        'awayTeam.type.1','awayTeam.disabled.1',
        'homeTeam.subTeams.1','homeTeam.type.1',
        'homeTeam.disabled.1','tournament.category.slug.1',
        'hasGlobalHighlights.1','tournament.slug.1',
        'promotion.id','team.disabled',
        'descriptions','id',
        'awayTeam.subTeams','awayTeam.type',
        'awayTeam.disabled','homeTeam.subTeams'

    ]

    # Drop the columns if they exist
    columns_to_drop = [col for col in columns_to_drop if col in df.columns]
    df = df.drop(columns_to_drop, axis=1)

    # Write the dataframe back to the csv
    df.to_csv(f'Merged/Cleaned/merged_data_{id_value}.csv', index=False)
