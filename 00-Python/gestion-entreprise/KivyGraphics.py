from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics import Color,Rectangle,Line


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            # add your instruction for main canvas here
            #Dessine une ligne passant par les points
            Line(points=(x1,y1,x2,y2,x3,y3))
            #Carré rouge semi transparent
            Color(1, 0, 0, .5, mode='rgba')
            Rectangle(pos=self.pos, size=self.size)

        with self.canvas.before:
            # you can use this to add instructions rendered before
            Color(1, 0, .4, mode='rgb')

        with self.canvas.after:
            # you can use this to add instructions rendered after