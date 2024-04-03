from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name="page1" # name of screen for called later in  switch_prev for go back to home screen
        #container that will contain my widget of home screen
        self.home=BoxLayout(orientation="vertical")
        #container that contain label and zone of name, first name and mail
        self.inside = GridLayout(cols=2, size_hint=(1, .6))
        self.inside.add_widget(Label(text="Nom", font_size=20, bold=True))
        self.inp1 = TextInput(hint_text="Ecrire ton nom ici", font_size=20,multiline=False)
        self.inside.add_widget(self.inp1)

        self.inside.add_widget(Label(text="Prenom", font_size=20, bold=True))
        self.inp2 = TextInput(hint_text="Prenom", font_size=20,multiline=False)
        self.inside.add_widget(self.inp2)

        self.inside.add_widget(Label(text="E-mail", font_size=20, bold=True))
        self.inp3 = TextInput(hint_text="Ecire ton E-mail Ici", font_size=20,multiline=False)
        self.inside.add_widget(self.inp3)

        self.home.add_widget(self.inside)

        self.gridbtn=GridLayout(cols=1,rows=1,size_hint=(1,.2))

        self.btn=Button(text="Submit",font_size=25,color="red",background_color="grey")
        self.btn.bind(on_press=self.stockcordonnee)
        self.gridbtn.add_widget(self.btn)

        self.home.add_widget(self.gridbtn)

        # Create the Gridlayout for the Scroll View and add height bounding
        self.contend_scroll_grid = GridLayout(size_hint_y=None, row_default_height=60, cols=1)
        self.contend_scroll_grid.bind(minimum_height=self.contend_scroll_grid.setter('height'))
        # Add the contend to the Scroll View
        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.contend_scroll_grid)
        # Add the two Widgets to Home Screen
        self.home.add_widget(self.scroll_view)

        self.add_widget(self.home)

        self.loadUser()

    def loadUser(self):
        with open("file.txt","r") as file:
            lines=file.readlines()
        for line in lines:
            word=line.split()
            self.btnuser=Button(text=word[0] + " | " + word[1] + " | " + word[2], font_size=20)
            self.btnuser.bind(on_press=self.switch_next)
            self.contend_scroll_grid.add_widget(self.btnuser)

    def stockcordonnee(self, *args):
        if self.inp1.text !="" and self.inp2.text !="" and self.inp3.text !="":
            with open("file.txt", "a") as file:
                file.writelines("{} {} {}\n".format(self.inp1.text, self.inp2.text, self.inp3.text))
            self.btnnewuser=Button(text=self.inp1.text+" | "+self.inp2.text+" | "+self.inp3.text,font_size=20)
            self.btnnewuser.bind(on_press=self.switch_next)
            self.contend_scroll_grid.add_widget(self.btnnewuser)
            self.inp1.text=""
            self.inp2.text=""
            self.inp3.text=""
            self.switch_next()
        else:
            self.popfunction()
    def popfunction(self):
        self.box=BoxLayout(orientation="vertical")
        self.box.add_widget(Label(text="il faut remplir tous les champs",font_size=17))
        self.btnpop=Button(text="Ok", color="red", font_size=15, size_hint=(.35, .35), pos_hint={'center_x': 0.5})
        self.box.add_widget(self.btnpop)
        self.pop=Popup(title="Info", content=self.box,size_hint=(None,None),
                size=(250,200),auto_dismiss=False,
                title_size=30,title_color="green",title_align="center" )
        self.btnpop.bind(on_press=self.pop.dismiss)
        self.pop.open()

    def switch_next(self,*args):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = Screentwo().name

class Screentwo(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name="page2"
        #self.secondescreen = BoxLayout(orientation="vertical")
        self.insidebtn = GridLayout(cols=5, size_hint=(.2, .3))

        self.img = Image(source="download.jpeg")
        self.insidebtn.add_widget(self.img)

        self.btnmenu = Button(text="Menu Connexion", font_size=20, size_hint=(0.2, .12), bold=True, color="yellow")
        self.btnmenu.bind(on_press=self.switch_prev)
        self.insidebtn.add_widget(self.btnmenu)
        self.add_widget(self.insidebtn)

        self.btnup = Button(text="Haut", font_size=15, size_hint=(None, None), bold=True, color="white")
        self.btnup.bind(on_press=self.switch_prev)
        self.insidebtn.add_widget(self.btnup)
        self.add_widget(self.insidebtn)

        #self.secondescreen.add_widget(self.insidebtn)
        self.add_widget(self.insidebtn)

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current =HomeScreen().name

class Navigate(ScreenManager):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen())
        self.add_widget(Screentwo())

class MyHomeWindow(App):
    def build(self):
        return Navigate()

if __name__ == '__main__':
    MyHomeWindow().run()
