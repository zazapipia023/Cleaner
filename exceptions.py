import requests
import json
from logging_config import logger

# BASE_URL = "http://localhost:8080/exceptions/"
#
#
# def get_exceptions(platform):
#     url = f"{BASE_URL}{platform}"
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         return json.loads(r.text)
#     except Exception as e:
#         logger.error(f"Failed to fetch exceptions for {platform}: {e}")
#         return []


def get_steam_exceptions():
    return ['dota 2 beta', 'PUBG', 'Steamworks Shared', 'Counter-Strike Global Offensive',
            'War Thunder', 'Apex Legends', 'Grand Theft Auto V', 'Call of Duty HQ']
    # return get_exceptions("steam")


def get_manifest_exceptions():
    return ['570', '578080', '730', '236390', '1172470', '271590', '1962663']
    # return get_exceptions("manifest")


def get_egs_exceptions():
    return ['DirectXRedist', 'Launcher', 'Fortnite', 'GTAV', 'GenshinImpact']
    # return get_exceptions("epic")


def get_vk_exceptions():
    return ['Warface', 'VKPlayCloud', 'Distrib', 'ArcheAge']
    # return get_exceptions("vk")


def get_battlenet_exceptions():
    return ['Hearthstone', 'Overwatch']
    # return get_exceptions("battlenet")
