import psutil
import requests
import socket
import logging.config

hostname = socket.gethostname()
logging.info("Got hostname: " + hostname)
IP = socket.gethostbyname(hostname)
logging.info("Got IP: " + IP)


def get_total_disk_space(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        total_space = disk_usage.total
        logging.info("Got info about total disk space: " + total_space)
        return total_space
    except FileNotFoundError:
        logging.error("Disk " + disk + " not found")
        return None


def get_free_disk_space(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        free_space = disk_usage.free
        logging.info("Got info about free disk space: " + free_space)
        return free_space
    except FileNotFoundError:
        logging.error("Disk " + disk + " not found")
        return None


def send_disk_info(space_before, space_after):
    total_space = get_total_disk_space(r"D:")
    total_space = int(total_space / (1024 ** 3))
    space_before = int(space_before / (1024 ** 3))
    space_after = int(space_after / (1024 ** 3))

    report = {'club_id': "68-1",
              'totals': total_space,
              'free_b': space_before,
              'free_a': space_after,
              'pc': hostname,
              'ip': IP}

    url = f"http://81.200.145.178:8080/sendReport"
    logging.info("Sending report on url: " + url +
                 "\nJSON: " + report)
    r = requests.post(url, json=report)
    logging.info("Sent report about cleaning. Status: " + r.text)
