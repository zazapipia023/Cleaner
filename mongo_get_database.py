from pymongo import MongoClient
import logging.config


def get_database():
    connection_string = ("mongodb url here")
    logging.info("Connecting do MongoDB")
    client = MongoClient(connection_string)
    return client['colizeum_db']
