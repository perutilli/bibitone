from lib.Liquid import *
from lib.Drink import *

from kivy.config import Config

import json

config_file = "data/config.json"

pump_rate = 0
bic_size = 0
shot_size = 0
resolution = (0, 0)

with open(config_file) as data_file:
    data = json.load(data_file)
    pump_rate = data["pump_rate"]
    bic_size = data["bic_size"]
    shot_size = data["shot_size"]
    resolution = (data["resolution"][0], data["resolution"][1])


liquids_file = "data/liquids.json"
drinks_file = "data/drinks.json"

liquids = []
drinks = []


def decode_liquid(dict):
    return Liquid(dict["name"], dict["position"])


def decode_drink(dict):
    quantities = {}
    for liq in dict["liquids"]:
        liq_name = liq["name"]
        for l in liquids:
            if (l.name == liq_name):
                quantities[l] = liq["portion"]
                break
    return Drink(dict["name"], quantities)


with open(liquids_file) as data_file:
    data = data_file.read()
    liquids = json.loads(data, object_hook=decode_liquid)

with open(drinks_file) as data_file:
    for drink in json.load(data_file):
        drinks.append(decode_drink(drink))


# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'borderless', True)

# fix the width of the window
Config.set('graphics', 'width', resolution[0])

# fix the height of the window
Config.set('graphics', 'height', resolution[1])
