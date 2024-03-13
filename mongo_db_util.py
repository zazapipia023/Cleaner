from mongo_get_database import get_database


def get_egs_games(club_id):
    dbname = get_database()
    collection_name = dbname["club"]
    games = collection_name.find_one({"clubId": club_id})
    return games['egsGames']


def get_steam_games(club_id):
    dbname = get_database()
    collection_name = dbname["club"]
    games = collection_name.find_one({"clubId": club_id})
    return games['steamGames']

