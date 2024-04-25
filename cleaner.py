import os
import shutil
import exceptions
import re
from logging_config import logger


def clean_dir(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            logger.info(f"Deleting file/directory, path: {file_path}")
            if os.path.isdir(file_path) and os.path.exists(file_path):
                shutil.rmtree(file_path)
                logger.info(f"Deleted directory, path: {file_path}")
            if os.path.isfile(file_path) and os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Deleted file, path: {file_path}")
        except OSError as e:
            logger.error(f"Error on delete, path: {file_path}: {e}")


def clean_dir_with_exceptions(directory, exceptions, content_folder='none', regex_exceptions=None):
    for dir_folder in os.listdir(directory):
        dir_path = os.path.join(directory, dir_folder)
        dir_name = dir_path
        if content_folder != 'none':
            dir_name = dir_path.replace(content_folder, '')
        if dir_name in exceptions:
            continue
        else:
            if regex_exceptions and any(re.match(regex, dir_name) for regex in regex_exceptions):
                continue
            try:
                logger.info(f"Deleting file/directory, path: {dir_path}")
                if os.path.isdir(dir_path) and os.path.exists(dir_path):
                    shutil.rmtree(dir_path)
                    logger.info(f"Deleted directory, path: {dir_path}")
                if os.path.isfile(dir_path) and os.path.exists(dir_path):
                    os.remove(dir_path)
                    logger.info(f"Deleted file, path: {dir_path}")
            except OSError as e:
                logger.error(f"Error on delete, path: {dir_path}: {e}")


def clean_root_dir():
    try:
        logger.info("Cleaning disk root directory has started")
        root_dirs = [r"D:\ChromeDownloads", r"D:\ColizeumUtil", r"D:\Games", r"D:\AacKBSetup", r"D:\Загрузки uFiler"]
        folder_to_clean = "D:\\"
        clean_dir_with_exceptions(folder_to_clean, root_dirs)
        logger.info("Cleaning disk root directory is complete")
    except Exception as e:
        logger.error(f"An error occurred during root folder cleaning: {e}")


def clean_games_root_dir():
    try:
        logger.info("Cleaning games root directory has started")
        games_root_dirs = [r"D:\Games\Battle.net", r"D:\Games\BsgLauncher", r"D:\Games\Epic Games",
                           r"D:\Games\Game Centre", r"D:\Games\Lesta", r"D:\Games\Portable", r"D:\Games\Riot Games",
                           r"D:\Games\Rockstar Games", r"D:\Games\Steam", r"D:\Games\Tanki", r"D:\Games\Tanks_Blitz",
                           r"D:\Games\Ubisoft Game Launcher", r"D:\Games\WarThunder", r"D:\Games\tarkov"]
        folder_to_clean = r"D:\Games"
        clean_dir_with_exceptions(folder_to_clean, games_root_dirs)
        logger.info("Cleaning games root directory is complete")
    except Exception as e:
        logger.error(f"An error occurred during games folder cleaning: {e}")

def clean_egs_content():
    try:
        logger.info("Cleaning EGS games has started")
        folder_to_clean = r"D:\Games\Epic Games"
        content_not_to_clean = exceptions.get_egs_exceptions()
        clean_dir_with_exceptions(folder_to_clean, content_not_to_clean, 'D:\\Games\\Epic Games\\')
        logger.info("Cleaning EGS games is complete")
    except Exception as e:
        logger.error(f"An error occurred during EGS content cleaning: {e}")


def clean_steam_content():
    try:
        logger.info("Cleaning steam games has started")
        folder_to_clean = r"D:\Games\Steam\steamapps\common"
        content_not_to_clean = exceptions.get_steam_exceptions()
        manifest_not_to_clean = exceptions.get_manifest_exceptions()
        clean_dir_with_exceptions(folder_to_clean, content_not_to_clean, 'D:\\Games\\Steam\\steamapps\\common\\')
        clean_manifest_files(manifest_not_to_clean)
        logger.info("Cleaning steam games is complete")
    except Exception as e:
        logger.error(f"An error occurred during Steam content cleaning: {e}")


def clean_manifest_files(acf_arr):
    logger.info("Cleaning steam manifest files has started")
    directory = r"D:\Games\Steam\steamapps"
    for file in os.listdir(directory):
        is_delete = True
        file_path = os.path.join(directory, file)
        for acf in acf_arr:
            logger.info(f"Checking is {acf} in {file_path}")
            if acf in file_path:
                logger.info(f"{acf} in exceptions, can't be deleted")
                is_delete = False
                break
        if is_delete:
            logger.info(f"{acf} not in exceptions, trying to delete")
            try:
                if os.path.isfile(file_path) and os.path.exists(file_path) and "vdf" not in file_path:
                    os.remove(file_path)
                    logger.info(f"Deleted file, path: {file_path}")
            except OSError as e:
                logger.error(f"Error on delete, path: {file_path}: {e}")
    logger.info("Cleaning steam manifest files is complete")


def clean_chrome_downloads():
    try:
        logger.info("Cleaning chrome downloads has started")
        folder_to_clean = r"D:\ChromeDownloads"
        clean_dir(folder_to_clean)
        logger.info("Cleaning chrome downloads is complete")
    except Exception as e:
        logger.error(f"An error occurred during Chrome downloads cleaning: {e}")


def clean_steam_workshop_content():
    try:
        logger.info("Cleaning workshop content has started")
        folder_to_clean = r"D:\Games\Steam\steamapps\workshop"
        clean_dir(folder_to_clean)
        logger.info("Cleaning workshop content is complete")
    except Exception as e:
        logger.error(f"An error occurred during Steam workshop content cleaning: {e}")


def clean_steam_downloading_content():
    try:
        logger.info("Cleaning downloading steam content has started")
        folder_to_clean = r"D:\Games\Steam\steamapps\downloading"
        clean_dir(folder_to_clean)
        logger.info("Cleaning downloading steam content is complete")
    except Exception as e:
        logger.error(f"An error occurred during Steam downloading content cleaning: {e}")


def clean_vk_play_content():
    try:
        logger.info("Cleaning VK Play content has started")
        folder_to_clean = r"D:\Games\Game Centre"
        content_not_to_clean = exceptions.get_vk_exceptions()
        clean_dir_with_exceptions(folder_to_clean, content_not_to_clean, 'D:\\Games\\Game Centre\\')
        logger.info("Cleaning VK Play content is complete")
    except Exception as e:
        logger.error(f"An error occurred during VK Play content cleaning: {e}")


def clean_ubisoft_content():
    try:
        logger.info("Cleaning Ubisoft Games content has started")
        folder_to_clean = r"D:\Games\Ubisoft Game Launcher\games"
        content_not_to_clean = exceptions.get_ubisoft_exceptions()
        if os.path.exists(folder_to_clean):
            clean_dir_with_exceptions(folder_to_clean, content_not_to_clean,
                                      'D:\\Games\\Ubisoft Game Launcher\\games\\')
        logger.info("Cleaning Ubisoft Games content is complete")
    except Exception as e:
        logger.error(f"An error occurred during Ubisoft content cleaning: {e}")


def clean_battlenet_content():
    try:
        logger.info("Cleaning Battle Net content has started")
        folder_to_clean = r"D:\Games\Battle.net"
        content_not_to_clean = exceptions.get_battlenet_exceptions()
        clean_dir_with_exceptions(folder_to_clean, content_not_to_clean, 'D:\\Games\\Battle.net\\',
                                  ['^\.battle\.net$|^Battle\.net\.\d+$|^Battle\.net '
                                   'Launcher$|^Battle\.net\.exe$|^Battle\.net '
                                   'Launcher\.exe$|\.patch\.result$|\.product\.db$|Launcher\.db$|Microsoft\.Gaming'
                                   '\.XboxApp\.Extensions\.winmd$'])
        logger.info("Cleaning Battle Net content is complete")
    except Exception as e:
        logger.error(f"An error occurred during Battle Net content cleaning: {e}")


def clean():
    clean_chrome_downloads()
    clean_steam_workshop_content()
    clean_steam_downloading_content()
    clean_steam_content()
    clean_egs_content()
    clean_vk_play_content()
    clean_ubisoft_content()
    clean_battlenet_content()
    clean_games_root_dir()
    clean_root_dir()
