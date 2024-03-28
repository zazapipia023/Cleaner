import psutil
import requests
import socket
from logging_config import logger

hostname = socket.gethostname()
logger.info("Got hostname")
IP = socket.gethostbyname(hostname)
logger.info("Got IP")


def get_total_disk_space(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        total_space = disk_usage.total
        logger.info("Got info about total disk space")
        return total_space
    except FileNotFoundError:
        logger.error("Disk " + disk + " not found")
        return None


def get_free_disk_space(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        free_space = disk_usage.free
        logger.info("Got info about free disk space")
        return free_space
    except FileNotFoundError:
        logger.error("Disk " + disk + " not found")
        return None


def send_disk_info(space_before, space_after):
    total_space = get_total_disk_space(r"D:")
    total_space = int(total_space / (1024 ** 3))
    space_before = int(space_before / (1024 ** 3))
    space_after = int(space_after / (1024 ** 3))

    report = {'club_id': "253-0",
              'totals': total_space,
              'free_b': space_before,
              'free_a': space_after,
              'pc': hostname,
              'ip': IP}

    url = f"http://81.200.145.178:8080/report"
    logger.info("Sending report")
    r = requests.post(url, json=report)
    logger.info("Sent report about cleaning. Status: " + r.text)
