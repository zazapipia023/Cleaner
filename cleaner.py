import os
import shutil

import mongo_db_util


def clean_dir(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            print(f"Удаление {file_path}")
            if os.path.isdir(file_path) and os.path.exists(file_path):
                shutil.rmtree(file_path)
                print(f"Удалена папка {file_path}")
            elif os.path.isfile(file_path) and os.path.exists(file_path):
                os.remove(file_path)
                print(f"Удален файл {file_path}")
        except OSError as e:
            print(f"Ошибка удаления {file_path}: {e}")


def clean_dir_with_exceptions(directory, exceptions, games_folder='none'):
    for dir_folder in os.listdir(directory):
        dir_path = os.path.join(directory, dir_folder)
        dir_name = dir_path
        if games_folder != 'none':
            dir_name = dir_path.replace(games_folder, '')
        if dir_name in exceptions:
            continue
        else:
            try:
                print(f"Удаление {dir_path}")
                if os.path.isdir(dir_path) and os.path.exists(dir_path):
                    shutil.rmtree(dir_path)
                    print(f"Удалена папка {dir_path}")
                if os.path.isfile(dir_path) and os.path.exists(dir_path):
                    os.remove(dir_path)
                    print(f"Удален файл {dir_path}")
            except OSError as e:
                print(f"Ошибка удаления {dir_path}: {e}")


def clean_root_dir():
    root_dirs = [r"D:\ChromeDownloads", r"D:\ColizeumUtil", r"D:\Games",
                 r"D:\Игры", r"D:\Клубные аккаунты.lnk", r"D:\Игры без аккаунтов.lnk"]
    folder_to_clean = "D:\\"
    clean_dir_with_exceptions(folder_to_clean, root_dirs)


def clean_games_root_dir():
    games_root_dirs = [r"D:\Games\Battle.net", r"D:\Games\BsgLauncher", r"D:\Games\Epic Games",
                       r"D:\Games\Game Centre", r"D:\Games\Genshin Impact", r"D:\Games\Innova",
                       r"D:\Games\Lesta", r"D:\Games\Minecraft", r"D:\Games\Portable", r"D:\Games\Riot Games",
                       r"D:\Games\Rockstar Games", r"D:\Games\Steam", r"D:\Games\Tanki",
                       r"D:\Games\Ubisoft Game Launcher",
                       r"D:\Games\tarkov", r"D:\Games\RAGEMP"]
    folder_to_clean = r"D:\Games"
    clean_dir_with_exceptions(folder_to_clean, games_root_dirs)


def clean_egs_games():
    folder_to_clean = r"D:\Games\Epic Games"
    games_not_to_clean = mongo_db_util.get_egs_games("141-0")
    clean_dir_with_exceptions(folder_to_clean, games_not_to_clean, 'D:\\Games\\Epic Games\\')


def clean_steam_games():
    folder_to_clean = r"D:\Games\Steam\steamapps\common"
    games_not_to_clean = mongo_db_util.get_steam_games("141-0")
    clean_dir_with_exceptions(folder_to_clean, games_not_to_clean.keys(), 'D:\\Games\\Steam\\steamapps\\common\\')
    clean_manifest_files(games_not_to_clean.values())


def clean_manifest_files(acf_arr):
    directory = r"D:\Games\Steam\steamapps"
    for file in os.listdir(directory):
        is_delete = True
        file_path = os.path.join(directory, file)
        for acf in acf_arr:
            if acf in file_path:
                is_delete = False
                break
        if is_delete:
            try:
                if os.path.isfile(file_path) and os.path.exists(file_path) and "vdf" not in file_path:
                    os.remove(file_path)
                    print(f"Удален файл {file_path}")
            except OSError as e:
                print(f"Ошибка удаления {file_path}: {e}")


def clean_chrome_downloads():
    folder_to_clean = r"D:\ChromeDownloads"
    clean_dir(folder_to_clean)


def clean_steam_workshop_content():
    folder_to_clean = r"D:\Games\Steam\steamapps\workshop"
    for dir_content in os.listdir(folder_to_clean):
        full_path = os.path.join(folder_to_clean, dir_content)
        clean_dir(full_path)


def clean_steam_downloading_content():
    folder_to_clean = r"D:\Games\Steam\steamapps\downloading"
    clean_dir(folder_to_clean)


def clean():
    clean_chrome_downloads()
    clean_steam_workshop_content()
    clean_steam_downloading_content()
    clean_steam_games()
    clean_egs_games()
    clean_games_root_dir()
    clean_root_dir()
