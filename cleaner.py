import os
import urllib.request
import shutil

import psutil

import googledoc


def clean_dir(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            print(f"Удаление {file_path}")
            if os.path.isdir(file_path) and os.path.exists(file_path):
                shutil.rmtree(file_path)
                print(f"Удалена папка {file_path}")
            if os.path.isfile(file_path) and os.path.exists(file_path):
                os.remove(file_path)
                print(f"Удален файл {file_path}")
        except OSError as e:
            print(f"Ошибка удаления {file_path}: {e}")


def clean_root_dir():
    root_dirs = [r"D:\ChromeDownloads", r"D:\ColizeumUtil", r"D:\Games",
                 r"D:\Игры", r"D:\Клубные аккаунты.lnk", r"D:\Игры без аккаунтов.lnk"]
    root_dir = r"D:"
    for file in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file)
        if file_path in root_dirs:
            continue
        else:
            try:
                print(f"Удаление {file_path}")
                if os.path.isdir(file_path) and os.path.exists(file_path):
                    shutil.rmtree(file_path)
                    print(f"Удалена папка {file_path}")
                if os.path.isfile(file_path) and os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Удален файл {file_path}")
            except OSError as e:
                print(f"Ошибка удаления {file_path}: {e}")


def clean_games_root_dir():
    games_root_dirs = [r"D:\Games\Battle.net", r"D:\Games\BsgLauncher", r"D:\Games\Epic Games",
                       r"D:\Games\Game Centre", r"D:\Games\Genshin Impact", r"D:\Games\Innova",
                       r"D:\Games\Lesta", r"D:\Games\Minecraft", r"D:\Games\Portable", r"D:\Games\Riot Games",
                       r"D:\Games\Rockstar Games", r"D:\Games\Steam", r"D:\Games\Tanki",
                       r"D:\Games\Ubisoft Game Launcher",
                       r"D:\Games\tarkov", r"D:\Games\RAGEMP"]
    root_dir = r"D:\Games"
    for file in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file)
        if file_path in games_root_dirs:
            continue
        else:
            try:
                print(f"Удаление {file_path}")
                if os.path.isdir(file_path) and os.path.exists(file_path):
                    shutil.rmtree(file_path)
                    print(f"Удалена папка {file_path}")
                if os.path.isfile(file_path) and os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Удален файл {file_path}")
            except OSError as e:
                print(f"Ошибка удаления {file_path}: {e}")


def clean_chrome_downloads():
    dir_chrome_downloads = r"D:\ChromeDownloads"
    clean_dir(dir_chrome_downloads)


def clean_steam_workshop_content():
    dir_workshop_content = r"D:\Games\Steam\steamapps\workshop\content"
    for dir_content in os.listdir(dir_workshop_content):
        full_path = os.path.join(dir_workshop_content, dir_content)
        clean_dir(full_path)


def clean_steam_downloading_content():
    dir_steam_downloading = r"D:\Games\Steam\steamapps\downloading"
    clean_dir(dir_steam_downloading)


def clean_games():
    paths_to_clean = [r"D:\Games\Steam\steamapps\common", r"D:\Games\Epic Games"]
    paths_not_to_clean = googledoc.get_paths_from_doc()

    for directory in paths_to_clean:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if r"D:\Games\Steam\steamapps\common" in file_path:
                file_name = file_path.replace('D:\\Games\\Steam\\steamapps\\common\\', '')
            if r"D:\Games\Epic Games" in file_path:
                file_name = file_path.replace('D:\\Games\\Epic Games\\', '')
            if file_name in paths_not_to_clean:
                continue
            else:
                try:
                    print(f"Удаление {file_path}")
                    if os.path.isdir(file_path) and os.path.exists(file_path):
                        shutil.rmtree(file_path)
                        print(f"Удалена папка {file_path}")
                    if os.path.isfile(file_path) and os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"Удален файл {file_path}")
                except OSError as e:
                    print(f"Ошибка удаления {file_path}: {e}")


def get_games_not_to_clean():
    file_id = "1Ht8-2e7u69lbRYoU4VQR2XJUbuz2DgwV"
    url = f"https://drive.google.com/uc?id={file_id}"

    file_name = "no_clean.txt"

    try:
        urllib.request.urlretrieve(url, file_name)
        print(f"Файл успешно скачан: {file_name}")
    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")


# def read_file(file_name):
#     try:
#         with open(file_name, "r") as file:
#             for line in file:
#                 line_data = line.strip()
#                 paths_not_to_clean.append(line_data)
#     except FileNotFoundError:
#         print(f"Файл '{file_name}' не найден.")
#     except Exception as e:
#         print(f"Ошибка при чтении файла: {e}")

x = input("1 - Полная очистка\n2 - Очистка без удаления steam workshop файлов\n")


def get_disk_info(disk):
    try:
        disk_usage = psutil.disk_usage(disk)
        total_space = disk_usage.total
        free_space = disk_usage.free
        return total_space, free_space
    except FileNotFoundError:
        return None, None


total_space, free_space = get_disk_info(r"D:")

print("Перед очисткой:")
if total_space is not None and free_space is not None:
    print(f"Общий размер диска D: {total_space / (1024 ** 3):.2f} GB")  # Переводим в гигабайты
    print(f"Свободное пространство на диске D: {free_space / (1024 ** 3):.2f} GB")  # Переводим в гигабайты
else:
    print("Диск D не найден.")

if x == '1':
    # clean_chrome_downloads()
    clean_steam_workshop_content()
    clean_steam_downloading_content()
    clean_games()
    clean_games_root_dir()
    clean_root_dir()
if x == '2':
    # clean_chrome_downloads()
    clean_steam_downloading_content()
    clean_games()
    clean_games_root_dir()
    clean_root_dir()

total_space, free_space = get_disk_info(r"D:")

print("После очистки")
if total_space is not None and free_space is not None:
    print(f"Общий размер диска D: {total_space / (1024 ** 3):.2f} GB")  # Переводим в гигабайты
    print(f"Свободное пространство на диске D: {free_space / (1024 ** 3):.2f} GB")  # Переводим в гигабайты
else:
    print("Диск D не найден.")

input("Нажмите Enter для выхода...")
