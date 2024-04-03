from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Bienvenue dans la simulation d'entreprise",
                size_hint=(.5, .2),
                pos_hint={'center_x': .5, 'center_y': .8}))
        self.add_widget(
            Button(
                text="Lancer simulation",
                size_hint=(.3, .1),
                pos_hint={'center_x': .8, 'center_y': .1}))

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0.3, 0.5, 0, 0.8)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

MainApp().run()