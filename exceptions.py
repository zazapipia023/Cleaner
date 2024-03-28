import requests
import json

BASE_URL = "http://localhost:8080/exceptions/"


def get_exceptions(platform):
    url = f"{BASE_URL}{platform}?clubId=id"
    r = requests.get(url)
    return json.loads(r.text)


def get_steam_exceptions():
    return get_exceptions("steam")


def get_manifest_exceptions():
    return get_exceptions("manifest")


def get_egs_exceptions():
    return get_exceptions("egs")


def get_vk_exceptions():
    return get_exceptions("vk")


def get_ubisoft_exceptions():
    return get_exceptions("ubisoft")


def get_battlenet_exceptions():
    return get_exceptions("battlenet")
