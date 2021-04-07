# my classes
from Pages import MainPage, ShotsPage, DrinksPage, ProgressPage
import config
# kivy imports
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

liquids = config.liquids
drinks = config.drinks


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
        pm = PageManager(dp, sp, mp, pp)

        return pm


if __name__ == '__main__':
    BibitoneApp().run()
