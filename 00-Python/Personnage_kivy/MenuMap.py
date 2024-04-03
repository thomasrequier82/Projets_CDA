from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import UI
from personnage import Personnage
from MenuConnexion import MenuConnexionController as mmc

class MenuMapVue(FloatLayout):
    def __init__(self, controller, **kwargs):
        FloatLayout.__init__(self, **kwargs)
        self.controller = controller
        self.avatar = ""
        # Definition de map comme FloatLayout
        self.map = FloatLayout(size_hint=(1, 1))

        #self.add_widget(self.map)
        self.layout1()
        # Definition de grille inside composée de 8 colonnes (Bouton retor menu + haut , bas , gauche, droite)
        self.grid1 = GridLayout(cols=8, size_hint=(1, .15))
        self.layout2()

        self.add_widget(self.map)

    def layout1(self):
        # Ajout de l'image
        self.img = Image(source=self.avatar, size_hint=(.1, .1))
        # centrage de l'image sur l'écran
        self.img.pos_hint = {"center_x": .5, "center_y": .5}
        self.map.add_widget(self.img,index=0)

    def layout2(self):
        # Bouton Retour menu à gauche
        btn1 = UI.Bouton(text="Menu", font_size=18, color="white", background_color="grey")
        btn1.bind(on_press=self.clbk_menu_connexion)
        self.grid1.add_widget(btn1,index=1)

        # 3 Labels vides où on pourra rajouter des infos si nécessaires
        lbl1 = UI.Etiquette(text="Pos_hint (x, y)", font_size=15, bold=True)
        self.grid1.add_widget(lbl1)
        self.lblx = UI.Etiquette(text="init", font_size=15, bold=True)
        self.grid1.add_widget(self.lblx)
        self.lbly = UI.Etiquette(text="init", font_size=15, bold=True)
        self.grid1.add_widget(self.lbly)

        # Bouton haut qui fait monter l'image au clic
        btn2 = UI.Bouton(text="Haut", font_size=20, color="white", background_color="grey")
        btn2.bind(on_press=self.clbk_monter)
        self.grid1.add_widget(btn2)
        # Bouton Bas qui fait descendre l'image au clic
        btn3 = UI.Bouton(text="Bas", font_size=20, color="white", background_color="grey")
        btn3.bind(on_press=self.clbk_descendre)
        self.grid1.add_widget(btn3)
        # Bouton gauche qui fait
        btn4 = UI.Bouton(text="Gauche", font_size=20, color="white", background_color="grey")
        btn4.bind(on_press=self.clbk_gauche)
        self.grid1.add_widget(btn4)

        btn5 = UI.Bouton(text="Droite", font_size=20, color="white", background_color="grey")
        btn5.bind(on_press=self.clbk_droite)
        self.grid1.add_widget(btn5)

        self.map.add_widget(self.grid1,index=2)

    def clbk_menu_connexion(self, widget):
        self.controller.naviguer_menu_connexion()

    def clbk_monter(self, widget):
        self.controller.monter_personnage()

    def clbk_descendre(self, widget):
        self.controller.descendre_personnage()

    def clbk_gauche(self, widget):
        self.controller.gauche_personnage()

    def clbk_droite(self, widget):
        self.controller.droite_personnage()

    def clbk_avatar(self,widget):
        self.controller.recup_avatar()


class MenuMapController():
    def __init__(self, menus):
        self.menus = menus
        self.vue = MenuMapVue(self)
        self.avatar_name = ""
        self.vue.avatar = self.avatar_name

    def naviguer_menu_connexion(self):
        self.menus.afficher_menu(self.menus.menu_connexion)

    def monter_personnage(self):
        # On recalcule la position y
        print(self.vue.img.pos_hint["center_y"])
        self.vue.img.pos_hint["center_y"] = self.vue.img.pos_hint["center_y"] + 0.07
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.vue.img.pos_hint["center_y"] >= 1:
            self.vue.img.pos_hint["center_y"] = 0

        self.vue.lbly.text = str(self.vue.img.pos_hint["center_y"])
        self.vue.map.do_layout()

    def descendre_personnage(self):
        self.vue.do_layout(self.vue.img)
        # On recalcule la position y
        print(self.vue.img.pos_hint["center_y"])
        self.vue.img.pos_hint["center_y"] = self.vue.img.pos_hint["center_y"] - 0.07
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.vue.img.pos_hint["center_y"] <= 0:
            self.vue.img.pos_hint["center_y"] = 1

        self.vue.lbly.text = str(self.vue.img.pos_hint["center_y"])
        self.vue.map.do_layout(self.vue.img)

    def gauche_personnage(self):
        # On recalcule la position x
        print(self.vue.img.pos_hint["center_x"])
        self.vue.img.pos_hint["center_x"] = self.vue.img.pos_hint["center_x"] - 0.07
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.vue.img.pos_hint["center_x"] <= 0:
            self.vue.img.pos_hint["center_x"] = 1

        self.vue.lblx.text = str(self.vue.img.pos_hint["center_x"])
        self.vue.map.do_layout()

    def droite_personnage(self):
        # On recalcule la position x
        print(self.vue.img.pos_hint["center_x"])
        self.vue.img.pos_hint["center_x"] = self.vue.img.pos_hint["center_x"] + 0.07
        # On teste si image sort de l'écran et on la fait revenir en caroussel
        if self.vue.img.pos_hint["center_x"] >= 1:
            self.vue.img.pos_hint["center_x"] = 0

        self.vue.lblx.text = str(self.vue.img.pos_hint["center_x"])
        self.vue.map.do_layout()

    def recup_avatar(self):
        #On récupère le nom de l'avatar
        self.avatar_name =  mmc.avtr
        while test == True:
            pass