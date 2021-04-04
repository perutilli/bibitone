import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar

import threading
import time

import config
import pumps

Builder.load_file('layouts.kv')


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

        # TODO: needs to be dynamically set based on len(shots_list)

        self.grid = GridLayout()
        self.grid.cols = 3
        for i, shot in enumerate(self.shots):
            b = ButtonWithId(text=shot.name, id=i)
            b.bind(on_press=self.click)
            self.grid.add_widget(b)
        self.ids.shots_page_layout.add_widget(self.grid)

    def click(self, instance):
        pumps_thread = threading.Thread(
            target=pumps.dispense_shot, args=(self.shots[instance.id],))
        pumps_thread.start()
        pumps_thread.join()

    def back(self):
        self.parent.current = 'main_page'


class DrinksPage(Screen):
    def __init__(self, drinks_list, **kwargs):
        super(DrinksPage, self).__init__(**kwargs)
        self.drinks = drinks_list

        self.grid = GridLayout()
        self.grid.cols = 3
        for i, drink in enumerate(self.drinks):
            b = ButtonWithId(text=drink.name, id=i)
            b.bind(on_press=self.click)
            self.grid.add_widget(b)
        self.ids.drinks_page_layout.add_widget(self.grid)

    def click(self, instance):
        pumps_thread = threading.Thread(
            target=pumps.dispense_drink, args=(self.drinks[instance.id],))
        pumps_thread.start()
        pumps_thread.join()

    def back(self):
        self.parent.current = 'main_page'


# class ProgressPage(Screen):
#     def __init__(self):
#         super(ProgressPage, self).__init__(**kwargs)
#         self.pb = ProgressBar(max=1000)
#         self.add_widget(self.pb)

#     def start_prog(self, time_len):
#         self.time_len = time_len
#         self.pb.value = 0
#         pb_thread = threading.Thread(
#             target=self.update_prog_bar, args=())
#         pb_thread.start()
#         pb_thread.join()

#     def update_prog_bar(self):
#         time_delta = self.time_len/1000
#         time.sleep(time_delta)
#         self.pb.value += 1
