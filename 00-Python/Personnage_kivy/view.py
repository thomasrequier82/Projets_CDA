from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from Personnage import Personnage
from kivy.animation import Animation
from kivy.uix.scatter import ScatterPlane

class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name="page1" # name of screen for called later in  switch_prev for go back to home screen
        #Definition de map comme FloatLayout
        self.map=FloatLayout(size_hint=(1,1))
        #Ajout de l'image
        self.img = Image(source="pomme.png",size_hint=(.1,.1))
        #centrage de l'image sur l'écran
        self.img.pos_hint = {"center_x":.5, "center_y":.5}
        self.map.add_widget(self.img)

        #Definition de grille inside composée de 8 colonnes (Bouton retor menu + haut , bas , gauche, droite)
        self.inside = GridLayout(cols=8, size_hint=(1, .15))
        #Bouton Retour menu à gauche
        self.btn1 = Button(text="Menu", font_size=18, color="white", background_color="grey")
        #self.btn1.bind(on_press=None)
        self.inside.add_widget(self.btn1)
        #3 Labels vides où on pourra rajouter des infos si nécessaires
        self.inside.add_widget(Label(text="Pos_hint (x, y)", font_size=15, bold=True))
        self.labelx = Label(text="               ", font_size=15, bold=True)
        self.inside.add_widget(self.labelx)
        self.labely = Label(text="              ", font_size=15, bold=True)
        self.inside.add_widget(self.labely)
        #Bouton haut qui fait monter l'image au clic
        self.btn2 = Button(text="Haut", font_size=20, color="white", background_color="grey")
        self.btn2.bind(on_press=self.monter)
        self.inside.add_widget(self.btn2)
        #Bouton Bas qui fait descendre l'image au clic
        self.btn3 = Button(text="Bas", font_size=20, color="white", background_color="grey")
        self.btn3.bind(on_press=self.descendre)
        self.inside.add_widget(self.btn3)
        #Bouton gauche qui fait
        self.btn4 = Button(text="Gauche", font_size=20, color="white", background_color="grey")
        self.btn4.bind(on_press=self.gauche)
        self.inside.add_widget(self.btn4)

        self.btn5 = Button(text="Droite", font_size=20, color="white", background_color="grey")
        self.btn5.bind(on_press=self.droite)
        self.inside.add_widget(self.btn5)

        self.map.add_widget(self.inside)


        self.add_widget(self.map)


    def monter(self,nut):
        # On recalcule la position y
        print(self.img.pos_hint["center_y"])
        self.img.pos_hint["center_y"]=self.img.pos_hint["center_y"]+0.05
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.img.pos_hint["center_y"] >= 1:
            self.img.pos_hint["center_y"] = 0

        self.labely.text = str(self.img.pos_hint["center_y"])
        self.bind(pos_hint=self.update_Widgt)
        self.do_layout()

        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(100, 200), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        animation.start(nut)

    def descendre(self,nut):
        #On recalcule la position y
        self.img.pos_hint["center_y"] = self.img.pos_hint["center_y"] - 0.05

        #On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.img.pos_hint["center_y"] == 0:
            self.img.pos_hint["center_y"] = 1
        self.labely.text = str(self.img.pos_hint["center_y"])
        self.bind(pos_hint=self.update_Widgt)
        self.do_layout()

        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(100, 200), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        animation.start(nut)

    def gauche(self,nut):
        self.img.pos_hint["center_x"] = self.img.pos_hint["center_x"] - 0.05
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.img.pos_hint["center_x"] == 0:
            self.img.pos_hint["center_x"] = 1

        self.labelx.text = str(self.img.pos_hint["center_x"])
        self.bind(pos_hint=self.update_Widgt)
        self.do_layout()

        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(100, 200), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.start(nut)

    def droite(self,nut):
        self.img.pos_hint["center_x"] = self.img.pos_hint["center_x"] + 0.05
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.img.pos_hint["center_x"] >= 1:
            self.img.pos_hint["center_x"] = 0

        self.labelx.text = str(self.img.pos_hint["center_x"])
        self.bind(pos_hint=self.update_Widgt)
        self.do_layout()

        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(100, 200), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        animation.start(nut)

    def update_Widgt(self, *args):
        #mise à jour de la position de l'image
        self.img.pos_hint["center_x","center_y"] = self.pos_hint["center_x","center_y"]

class Navigate(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen())
