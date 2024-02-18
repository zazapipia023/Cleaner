from mongo_get_database import get_database


def get_egs_games(club_id):
    dbname = get_database()
    collection_name = dbname["games_list"]
    games = collection_name.find_one({"_id": club_id})
    return games['games_egs']


def get_steam_games(club_id):
    dbname = get_database()
    collection_name = dbname["games_list"]
    games = collection_name.find_one({"_id": club_id})
    return games['games_steam']
