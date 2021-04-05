# my classes
from lib.Liquid import *
from lib.Drink import *
from Pages import MainPage, ShotsPage, DrinksPage, ProgressPage
# kivy imports
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
# python lib
import json

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


class PageManager(ScreenManager):
    def __init__(self, main_page, shots_page, drinks_page, progress_page, **kwargs):
        super(PageManager, self).__init__(**kwargs)
        self.main_page = main_page
        self.shots_page = shots_page
        self.drinks_page = drinks_page
        self.progress_page = progress_page
        self.add_widget(self.main_page)
        self.add_widget(self.shots_page)
        self.add_widget(self.drinks_page)
        self.add_widget(self.progress_page)


class BibitoneApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        mp = MainPage(name='main_page')
        sp = ShotsPage(liquids, name='shots_page')
        dp = DrinksPage(drinks, name='drinks_page')
        pp = ProgressPage(name='progress_page')
        pm = PageManager(mp, sp, dp, pp)

        return pm


if __name__ == '__main__':
    BibitoneApp().run()
