from kivy.app import App
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget

__version__ = '0.0.6'

class GameScreen(Widget):
    pass

class SettingsScreen(Widget):
    pass

class MancalaScreenManager(ScreenManager):
    pass

presentation = Builder.load_file('mancala.kv')

class MancalaApp(App):
    def build(self):
        return presentation
    
if __name__ == "__main__":
    MancalaApp().run()