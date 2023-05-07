import os
import time
import shutil

paths_not_to_clean = [
    r"D:\Games\Epic Games\Fortnite", r"D:\Games\Epic Games\DirectXRedist",
    r"D:\Games\Epic Games\GenshinImpact", r"D:\Games\Epic Games\Launcher",
    r"D:\Games\Steam\steamapps\common\Grand Theft Auto V",
    r"D:\Games\Steam\steamapps\common\dota 2 beta",
    r"D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive",
    r"D:\Games\Steam\steamapps\common\PUBG",
    r"D:\Games\Steam\steamapps\common\Apex Legends",
    r"D:\Games\Steam\steamapps\common\Call of Duty HQ"
]


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


def clean_useless_files():
    paths_to_clean = [r"D:\Games\Epic Games", r"D:\Games\Steam\steamapps\common"]

    for directory in paths_to_clean:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if file_path in paths_not_to_clean:
                continue
            else:
                if is_file_obsolete(file_path) and os.path.isdir(file_path) and os.path.exists(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted directory {file_path}")
                if os.path.isfile(file_path) and os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Deleted file {file_path}")


def is_file_obsolete(file_path):
    try:
            file_stat = os.stat(file_path)
            last_access_time = file_stat.st_atime
            file_age_in_days = (time.time() - last_access_time) / (
                    24 * 60 * 60)
            max_file_age_in_days = 15
            return file_age_in_days > max_file_age_in_days or os.path.getsize(
                file_path) == 0
    except Exception as e:
        print(f"Ошибка при проверке файла {file_path}: {e}")
        return False


clean_chrome_downloads()
clean_workshop_maps()
clean_steam_workshop_content()
clean_steam_downloading_content()
# clean_useless_files()