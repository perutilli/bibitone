from Liquid import *
from Drink import *
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Pages import MainPage, ShotsPage, DrinksPage
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


class BibitoneApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(ShotsPage(liquids, name='shots_page'))
        sm.add_widget(DrinksPage(drinks, name='drinks_page'))

        return sm


if __name__ == '__main__':
    BibitoneApp().run()
