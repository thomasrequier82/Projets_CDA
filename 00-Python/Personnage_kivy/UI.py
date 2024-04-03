from kivy.uix.label import Label
from kivy.uix.button import Button



class Texte(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.set_size)

    def set_size(self, widget, value):
        widget.text_size = self.size


class Bouton(Button):
    def __init__(self, color="red", **kwargs):
        Button.__init__(self, color=color, **kwargs)

class Etiquette(Label):
    def __init__(self, color="red", **kwargs):
        Label.__init__(self, color=color, **kwargs)