from datetime import datetime, timedelta
import mongo_db_util


def check_subscription():
    purchase_date = mongo_db_util.get_subscription("141-0")
    current_date = datetime.now()
    expiration_date = purchase_date + timedelta(days=30)

    return current_date > expiration_date
