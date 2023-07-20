import os
import urllib.request
import shutil

paths_not_to_clean = []


def clean_dir(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path) and os.path.exists(file_path):
            shutil.rmtree(file_path)
            print(f"Deleted directory {file_path}")
        if os.path.isfile(file_path) and os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file {file_path}")


def clean_chrome_downloads():
    dir_chrome_downloads = r"D:\ChromeDownloads"
    clean_dir(dir_chrome_downloads)


def clean_workshop_maps():
    dir_workshop_maps = r"D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\maps\workshop"
    clean_dir(dir_workshop_maps)


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
                if os.path.isdir(file_path) and os.path.exists(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted directory {file_path}")
                if os.path.isfile(file_path) and os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Deleted file {file_path}")


def get_games_not_to_clean():
    file_id = "1Ht8-2e7u69lbRYoU4VQR2XJUbuz2DgwV"
    url = f"https://drive.google.com/uc?id={file_id}"

    file_name = "no_clean.txt"

    try:
        urllib.request.urlretrieve(url, file_name)
        print(f"Файл успешно скачан: {file_name}")
    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_data = line.strip()
                paths_not_to_clean.append(line_data)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


get_games_not_to_clean()
read_file("no_clean.txt")
clean_chrome_downloads()
clean_workshop_maps()
clean_steam_workshop_content()
clean_steam_downloading_content()
clean_games()
