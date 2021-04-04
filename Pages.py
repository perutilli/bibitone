import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

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
        self.layout = GridLayout()
        # needs to be dynamically set based on len(shots_list)
        self.layout.cols = 3
        for shot in shots_list:
            self.layout.add_widget(Button(text=shot.name))

        self.add_widget(self.layout)


class DrinksPage(Screen):
    def __init__(self, drinks_list, **kwargs):
        super(DrinksPage, self).__init__(**kwargs)
        self.drinks = drinks_list
        self.layout = GridLayout()
        # needs to be dynamically set based on len(drinks_list)
        self.layout.cols = 3
        for i, drink in enumerate(drinks_list):
            b = ButtonWithId(text=drink.name, id=i)
            b.bind(on_press=self.click)
            self.layout.add_widget(b)

        self.add_widget(self.layout)

    def click(self, instance):
        print(self.drinks[instance.id])
