import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

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
        shot = self.shots[instance.id]
        t = pumps.calculate_time_shot(shot)
        pumps.dispense_shot(shot)
        self.parent.current = 'progress_page'
        self.parent.progress_page.start_prog(t, 'shots_page', shot)

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
        # pumps_thread = threading.Thread(
        #     target=pumps.dispense_drink, args=(self.drinks[instance.id],))
        # pumps_thread.start()
        # pumps_thread.join()
        drink = self.drinks[instance.id]
        t = pumps.calculate_time_drink(drink)
        pumps.dispense_drink(drink)
        self.parent.current = 'progress_page'
        self.parent.progress_page.start_prog(t, 'drinks_page', drink)

    def back(self):
        self.parent.current = 'main_page'


class ProgressPage(Screen):

    def start_prog(self, time_len, caller, liquid):
        self.time_len = time_len
        self.ids.prog_bar.value = 0
        self.caller = caller
        self.ids.display_name.text = str(liquid)
        self.start = time.time()  # time in seconds
        time_delta = self.time_len/self.ids.prog_bar.max
        Clock.schedule_interval(self.update_prog_bar, time_delta)
        # pb_thread = threading.Thread(
        #     target=self.update_prog_bar, args=())
        # pb_thread.start()
        # pb_thread.join()

    def update_prog_bar(self, dt):
        self.ids.prog_bar.value = (
            (time.time() - self.start) * self.ids.prog_bar.max) / (self.time_len)
        if(self.ids.prog_bar.value >= self.ids.prog_bar.max):
            Clock.unschedule(self.update_prog_bar)
            self.parent.current = self.caller
