from datetime import datetime, timedelta
import mongo_db_util
import logging.config


def check_subscription():
    purchase_date = mongo_db_util.get_subscription("68-1")
    logging.info("Got subscription date from club: " + purchase_date)
    current_date = datetime.now()
    expiration_date = purchase_date + timedelta(days=30)

    return current_date > expiration_date
