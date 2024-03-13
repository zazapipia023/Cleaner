import psutil
import requests
import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)


def get_total_disk_space(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        total_space = disk_usage.total
        return total_space
    except FileNotFoundError:
        return None


def get_free_disk_space(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        free_space = disk_usage.free
        return free_space
    except FileNotFoundError:
        return None


def send_disk_info(space_before, space_after):
    total_space = get_total_disk_space(r"D:")
    total_space = int(total_space / (1024 ** 3))
    space_before = int(space_before / (1024 ** 3))
    space_after = int(space_after / (1024 ** 3))

    report = {'club_id': "141-0",
              'totals': total_space,
              'free_b': space_before,
              'free_a': space_after,
              'pc': hostname,
              'ip': IP}

    url = f"http://localhost:8080/sendReport"
    r = requests.post(url, json=report)
    print("Report status: " + r.text)
