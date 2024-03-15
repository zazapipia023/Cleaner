from mongo_get_database import get_database


def get_egs_games(club_id):
    dbname = get_database()
    collection_name = dbname["club"]
    club = collection_name.find_one({"clubId": club_id})
    return club['egsGames']


def get_steam_games(club_id):
    dbname = get_database()
    collection_name = dbname["club"]
    club = collection_name.find_one({"clubId": club_id})
    return club['steamGames']


def get_subscription(club_id):
    dbname = get_database()
    collection_name = dbname["club"]
    club = collection_name.find_one({"clubId": club_id})
    return club['subDate']
