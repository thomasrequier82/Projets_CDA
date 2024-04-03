from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from MenuConnexion import MenuConnexionController
from MenuMap import MenuMapController

class Fenetre(GridLayout):
    def __init__(self, **kwargs):
        GridLayout.__init__(self, cols=1, rows=1, **kwargs)

    def afficher_menu(self, menu):
        self.clear_widgets()
        self.add_widget(menu)

class Menus():
    def __init__(self, **kwargs):
        self.fenetre = Fenetre()
        self.menu_connexion = MenuConnexionController(self)
        self.menu_map = MenuMapController(self)

        self.fenetre.afficher_menu(self.menu_connexion.vue)

    def afficher_menu(self, menu):
        self.fenetre.afficher_menu(menu.vue)



class Connexion(App):
    def build(self):
        menus = Menus()
        return menus.fenetre

if __name__ == '__main__':
    Connexion().run()

