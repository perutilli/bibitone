from Liquid import *
from Drink import *
import json
from types import SimpleNamespace

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


with open("liquids.json") as data_file:
    data = data_file.read()
    liquids = json.loads(data, object_hook=decode_liquid)

with open("drinks.json") as data_file:
    #data = data_file.read()
    for drink in json.load(data_file):
        drinks.append(decode_drink(drink))
