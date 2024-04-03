from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from main import main as m

class RootWidget(BoxLayout):

     def __init__(self, **kwargs):
         super(RootWidget, self).__init__(**kwargs)
         self.add_widget(Button(text='bouton 1'))
         cb = CustomBtn()
         cb.bind(pressed=self.btn_pressed)
         self.add_widget(cb)
         self.add_widget(Button(text='bouton 2'))

     def btn_pressed(self, instance, pos):
         print ('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn(Widget):

     pressed = ListProperty([0, 0])

     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             touch.grab(self)
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
             return True
         if touch.is_double_tap:
             m()
             """print('Touch is a double tap !')
             print(' - interval is', touch.double_tap_time)
             print(' - distance between previous is', touch.double_tap_distance)"""
         if touch.is_triple_tap:
             print('Touch is a triple tap !')
             print(' - interval is', touch.triple_tap_time)
             print(' - distance between previous is', touch.triple_tap_distance)
         return super(CustomBtn, self).on_touch_down(touch)

     def on_touch_up(self,touch):
         if touch.grab_current is self:
             print("Touché !")
             touch.ungrab(self)
             return True

     def on_pressed(self, instance, pos):
         print ('pressed at {pos}'.format(pos=pos))

class TestApp(App):

     def build(self):
         return RootWidget()


if __name__ == '__main__':
     TestApp().run()