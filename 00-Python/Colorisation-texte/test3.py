from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from functools import partial


class DemoBox(BoxLayout):

    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"

        btn = Button(text="Normal binding to event")
        btn.fbind('on_press', self.on_event)

        btn2 = Button(text="Normal binding to a property change")
        btn2.fbind('state', self.on_property)

        btn3 = Button(text="A: Using function with args.")
        btn3.fbind('on_press', self.on_event_with_args, 'right',
                       tree='birch', food='apple')

        btn4 = Button(text="Unbind A.")
        btn4.fbind('on_press', self.unbind_a, btn3)

        btn5 = Button(text="Use a flexible function")
        btn5.fbind('on_press', self.on_anything)

        btn6 = Button(text="B: Using flexible functions with args. For hardcores.")
        btn6.fbind('on_press', self.on_anything, "1", "2", monthy="python")

        btn7 = Button(text="Force dispatch B with different params")
        btn7.fbind('on_press', btn6.dispatch, 'on_press', 6, 7, monthy="other python")

        for but in [btn, btn2, btn3, btn4, btn5, btn6, btn7]:
            self.add_widget(but)

    def on_event(self, obj):
        print("Typical event from", obj)

    def on_event_with_args(self, side, obj, tree=None, food=None):
        print("Event with args", obj, side, tree, food)

    def on_property(self, obj, value):
        print("Typical property change from", obj, "to", value)

    def on_anything(self, *args, **kwargs):
        print('The flexible function has *args of', str(args),
            "and **kwargs of", str(kwargs))
        return True

    def unbind_a(self, btn, event):
        btn.funbind('on_press', self.on_event_with_args, 'right',
                        tree='birch', food='apple')


class DemoApp(App):
    def build(self):
        return DemoBox()


DemoApp().run()