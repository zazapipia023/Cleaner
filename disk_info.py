import psutil
import requests
import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)


def get_disk_info(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        total_space = disk_usage.total
        free_space = disk_usage.free
        return total_space, free_space
    except FileNotFoundError:
        return None, None


def send_disk_info():
    total_space, free_space = get_disk_info(r"D:")
    total_space = int(total_space / (1024 ** 3))
    free_space = int(free_space / (1024 ** 3))

    myobj = {'totals': total_space,
             'free': free_space,
             'pc': hostname,
             'ip': IP}
    print(myobj)

    if total_space is not None and free_space is not None:
        info = (f"Общий размер диска D: {total_space} GB\n"
                f"Свободное пространство на диске D: {free_space} GB")
        print(info)
        URL = f"http://localhost:8080/sendReport"
        r = requests.post(URL, json=myobj)
        print(r.text)
    else:
        print("Диск D не найден.")
