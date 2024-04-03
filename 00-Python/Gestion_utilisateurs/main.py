from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Ecran(BoxLayout):
    def __init__(self, **kwargs):
        super(Ecran,self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 30
        self.Un_Input()
        self.Un_Label()

        self.bouton_rouge = self.Un_Bouton("Rouge",0.5,0.2,"red")
        self.bouton_vert = self.Un_Bouton("Vert",0.5,0.5,"green")
        self.bouton_bleu = self.Un_Bouton("Bleu",0.5,0.9,"blue")
        self.bouton_jaune = self.Un_Bouton("Jaune",0.5,0.9,"yellow")
        self.bouton_rose = self.Un_Bouton("Rôse",0.5,0.9,"pink")
        self.bouton_marron = self.Un_Bouton("Marron",0.5,0.8,"brown")

    def Un_Bouton(self,couleur,droit,haut,couleurRGBA):
        # On cree un bouton:
        self.bouton1 = Button()
        # On lui donne des proprietes:
        # Un texte:
        self.bouton1.text = couleur
        # Une taille en pourcentages:
        self.bouton1.size_hint = (0.5, 0.15)
        # Une position:
        self.bouton1.pos_hint = {'right': droit,'top':haut}
        # Une couleur de fond:
        self.bouton1.background_color = couleurRGBA
        # On l'associe a une fonction:
        self.bouton1.bind(on_press=self.Une_Fonction_Bouton)
        # On l'ajoute au layout principal:
        self.add_widget(self.bouton1)

    def Un_Label(self):
        # On cree un label avec toutes ses proprietes:
        self.label1 = Label(text="Texte du label", font_size=30, color=[1, 0, 0, 1])
        # On l'ajoute au layout principal:
        self.add_widget(self.label1)

    def Un_Input(self):
        # On cree un Input avec des ses proprietes:
        self.input1 = TextInput(text="Entrez votre Texte", font_size=30)
        # On ajoute des proprietes (une largeur de 50% et une hauteur de 20%)
        self.input1.size_hint_x = 0.5
        self.input1.size_hint_y = 0.3
        # On l'ajoute au layout principal:
        self.add_widget(self.input1)

    def Une_Fonction_Bouton(self,instance):
        # la variable "instance" correspond au bouton qui a ete presse
        instance.color = 'white'
        # On peut changer le texte du label & sa couleur:
        self.label1.text = self.input1.text
        self.label1.color = instance.background_color
        # on reinitialiser le contenu du Input
        self.input1.text = "Entrez votre Texte"

class Menu(App):

    def build(self):
        Layout = Ecran()
        return Layout


if __name__ == '__main__':
    Menu().run()

