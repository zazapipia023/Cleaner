from mongo_get_database import get_database
import logging.config


def get_egs_games(club_id):
    dbname = get_database()
    logging.info("Requested colizeum_db from MongoDB")
    collection_name = dbname["club"]
    club = collection_name.find_one({"clubId": club_id})
    logging.info("Got data from club " + club_id)
    return club['egsGames']


def get_steam_games(club_id):
    dbname = get_database()
    logging.info("Requested colizeum_db from MongoDB")
    collection_name = dbname["club"]
    club = collection_name.find_one({"clubId": club_id})
    logging.info("Got data from club " + club_id)
    return club['steamGames']


def get_subscription(club_id):
    dbname = get_database()
    logging.info("Requested colizeum_db from MongoDB")
    collection_name = dbname["club"]
    club = collection_name.find_one({"clubId": club_id})
    logging.info("Got data from club " + club_id)
    return club['subDate']
