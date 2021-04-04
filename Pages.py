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
        self.layout = GridLayout()

        self.layout.cols = 1
        self.top_bar = GridLayout(
            size_hint_y=None,
            height=80
        )
        self.top_bar.cols = 2
        self.top_bar.add_widget(
            Button(
                text="back",
                size_hint_x=None,
                width=100,
                on_press=self.back
            )
        )
        self.top_bar.add_widget(
            Label(
                text="SHOTS"))
        self.layout.add_widget(self.top_bar)
        self.grid = GridLayout()
        self.grid.cols = 3
        for i, shot in enumerate(self.shots):
            b = ButtonWithId(text=shot.name, id=i)
            b.bind(on_press=self.click)
            self.grid.add_widget(b)
        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)

    def click(self, instance):
        pumps_thread = threading.Thread(
            target=pumps.dispense_shot, args=(self.shots[instance.id],))
        pumps_thread.start()
        pumps_thread.join()

    def back(self, instance):
        self.parent.current = 'main_page'


class DrinksPage(Screen):
    def __init__(self, drinks_list, **kwargs):
        super(DrinksPage, self).__init__(**kwargs)
        self.drinks = drinks_list
        self.layout = GridLayout()

        self.layout.cols = 1
        self.top_bar = GridLayout(
            size_hint_y=None,
            height=80
        )
        self.top_bar.cols = 2
        self.top_bar.add_widget(
            Button(
                text="back",
                size_hint_x=None,
                width=100,
                on_press=self.back
            )
        )
        self.top_bar.add_widget(
            Label(
                text="DRINKS"))
        self.layout.add_widget(self.top_bar)
        self.grid = GridLayout()
        self.grid.cols = 3
        for i, drink in enumerate(self.drinks):
            b = ButtonWithId(text=drink.name, id=i)
            b.bind(on_press=self.click)
            self.grid.add_widget(b)
        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)

    def click(self, instance):
        pumps_thread = threading.Thread(
            target=pumps.dispense_drink, args=(self.drinks[instance.id],))
        pumps_thread.start()
        pumps_thread.join()

    def back(self, instance):
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
