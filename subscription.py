from logging_config import logger
import requests


def check_subscription():
    logger.info("Checking subscription")
    url = f"http://81.200.145.178:8080/subscription?clubId=68-1"
    r = requests.get(url)
    return r.text
