import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

import threading
import time

import config
import pumps

Builder.load_file('layout.kv')


class ButtonWithId(Button):
    def __init__(self, id=-1, img_source="", **kwargs):
        super(ButtonWithId, self).__init__(**kwargs)
        self.id = id
        if(img_source != ""):
            self.image = Image(
                source=img_source,
            )
            self.add_widget(self.image)


class MainPage(Screen):
    pass


class ShotsPage(Screen):
    def __init__(self, shots_list, **kwargs):
        super(ShotsPage, self).__init__(**kwargs)
        self.shots = list(filter(lambda l: l.shot, shots_list))

        # TODO: needs to be dynamically set based on len(shots_list)

        self.grid = GridLayout()
        self.grid.cols = 2
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
        self.buttons = []
        for i, drink in enumerate(self.drinks):
            b = ButtonWithId(text=drink.name, id=i,
                             img_source=drink.img_source)
            b.bind(on_press=self.click, center=self.bind_images)
            self.grid.add_widget(b)
            self.buttons.append(b)
        self.ids.drinks_page_layout.add_widget(self.grid)

    def click(self, instance):
        drink = self.drinks[instance.id]
        t = pumps.calculate_time_drink(drink)
        pumps.dispense_drink(drink)
        self.parent.current = 'progress_page'
        self.parent.progress_page.start_prog(t, 'drinks_page', drink)

    def back(self):
        self.parent.current = 'main_page'

    def bind_images(self, instance, value):
        instance.image.size_hint = (None, None)
        instance.image.size = (0.9*instance.width, 0.9*instance.height)
        instance.image.center = value


class ProgressPage(Screen):

    def start_prog(self, time_len, caller, liquid):
        self.time_len = time_len
        self.max = 101
        # self.ids.prog_bar.value = 0
        self.caller = caller
        # self.ids.display_name.text = str(liquid)
        self.start = time.time()  # time in seconds
        time_delta = self.time_len/self.max
        Clock.schedule_interval(self.update_prog_bar, time_delta)

    def update_prog_bar(self, dt):
        frame_num = int(
            ((time.time() - self.start) * self.max) / (self.time_len)) + 1
        self.ids.prog_bar.source = f"atlas://images/prog_bar_atlas/ezgif-frame-{frame_num:03}"
        if(frame_num >= self.max):
            Clock.unschedule(self.update_prog_bar)
            self.parent.current = self.caller
