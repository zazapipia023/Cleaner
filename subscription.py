from logging_config import logger
import requests


def check_subscription():
    logger.info("Checking subscription")
    url = f"http://localhost:8080/subscription?clubId=id"
    r = requests.get(url)
    return r.text
