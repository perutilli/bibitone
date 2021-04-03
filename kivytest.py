import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('layouts.kv')


class MainPage(Screen):

    def press(self):
        pass


class ShotsPage(Screen):
    pass


class DrinksPage(Screen):
    pass


class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(ShotsPage(name='shots_page'))
        sm.add_widget(DrinksPage(name='drinks_page'))

        return sm


if __name__ == '__main__':
    MyApp().run()
