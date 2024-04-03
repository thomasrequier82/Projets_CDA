from kivymd.app import MDApp
from kivy.app import App
from controller import Controller
from model import MyScreenModel


class Calculatrice(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = MyScreenModel()
        self.controller =Controller()

    def build(self):
        return calcLayout()


Calculatrice().run()