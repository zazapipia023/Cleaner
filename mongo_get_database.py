from pymongo import MongoClient
from logging_config import logger


def get_database():
    connection_string = ("")
    logger.info("Connecting do MongoDB")
    client = MongoClient(connection_string)
    return client['colizeum_db']
