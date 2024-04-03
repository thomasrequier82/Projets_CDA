import json
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from observer import Observer
from kivy.uix.widget import Widget
from model import Modif
import constantes as C
from kivy.core.window import Window

# set window size
Window.size = (300, 450)

class View(BoxLayout):

    def __init__(self,**kwargs):
        """Constructeur"""
        super().__init__(**kwargs)
        self.controller = controller
        self._currentWindow = None
        self._user = None
        self.changeWindow("PytCalc1.09")

        self._make_main_frame()
        self._make_entry()

    def main(self):
        self.mainloop()



class Affich(TextInput):
    def createTextInput(self, texte):
        textInput = TextInput(size_hint=(1, .15), font_size=60, halign="right")
        textInput.bind(text=texte)
        self.add_widget(textInput)
        return textInput

class Touche(Button):
    def createButton(self, name: str, action):
        bouton = Button(text=name, size_hint=(.2, .2),font_size=32,on_press = action)
        self.add_widget(bouton)
        return bouton


class BoutonCalc(GridLayout):
    def init(self):
        GridLayout.__init__()
        self.cols = 4
        self.rows = 5
        Touche.createButton()