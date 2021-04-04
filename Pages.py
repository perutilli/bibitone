import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import threading
import time

Builder.load_file('layouts.kv')


def dispense_liquid():
    print("Opened pump")
    time.sleep(2)
    print("Closed pump")


class ButtonWithId(Button):
    def __init__(self, id=-1, **kwargs):
        super(ButtonWithId, self).__init__(**kwargs)
        self.id = id


class MainPage(Screen):

    def press(self):
        pass


class ShotsPage(Screen):
    def __init__(self, shots_list, **kwargs):
        super(ShotsPage, self).__init__(**kwargs)
        self.shots = shots_list
        self.layout = GridLayout()
        # needs to be dynamically set based on len(shots_list)
        self.layout.cols = 3
        for i, shot in enumerate(self.shots):
            b = ButtonWithId(text=shot.name, id=i)
            b.bind(on_press=self.click)
            self.layout.add_widget(b)

        self.add_widget(self.layout)

    def click(self, instance):
        thread = threading.Thread(
            target=dispense_liquid, args=())
        thread.start()
        thread.join()


class DrinksPage(Screen):
    def __init__(self, drinks_list, **kwargs):
        super(DrinksPage, self).__init__(**kwargs)
        self.drinks = drinks_list
        self.layout = GridLayout()
        # needs to be dynamically set based on len(drinks_list)
        self.layout.cols = 3
        for i, drink in enumerate(self.drinks):
            b = ButtonWithId(text=drink.name, id=i)
            b.bind(on_press=self.click)
            self.layout.add_widget(b)

        self.add_widget(self.layout)

    def click(self, instance):
        print(self.drinks[instance.id])
