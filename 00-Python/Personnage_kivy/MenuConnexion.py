from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics import Rectangle
import json

import UI
from personnage import Personnage



class MenuConnexionVue(GridLayout):
    def __init__(self, controller, **kwargs):
        GridLayout.__init__(self, cols=1, rows=6, **kwargs)
        self.controller = controller
        #Ecran de type Grille
        self.grid1 = GridLayout(cols=1)
        self.input_prenom = None
        self.avatar = ""
        self.avatar = []
        self.add_widget(self.grid1)
        self.layout1()
        #Ajout de champs  à 2 colonnes
        self.grid2 = GridLayout(cols=2, size_hint=(1, .6))
        self.grid_avatar = GridLayout(cols=8,size_hint=(1, .6))
        self.layout2()
        self.grid1.add_widget(self.grid2)
        self.gridbtn = GridLayout(cols=1,rows=1,size_hint=(1,.2))
        self.layout3()
        self.grid1.add_widget(self.gridbtn)
        self.contenu_scroll_grid = GridLayout(size_hint_y=None, row_default_height=60, cols=1)
        self.contenu_scroll_grid.bind(minimum_height=self.contenu_scroll_grid.setter('height'))
        self.layout4()
        self.add_widget(self.scroll_view)



    def layout1(self):
        self.grid1.clear_widgets()
        b1 = UI.Bouton(text="Menu Map")
        b1.bind(on_press=self.clbk_menu_images)
        self.grid1.add_widget(b1)


    def layout2(self):
        self.grid2.clear_widgets()
        self.grid2.add_widget(UI.Etiquette(text="Nom", font_size=20, bold=True))
        self.inp1 = TextInput(hint_text="Ecrire ton nom ici", font_size=20, multiline=False)
        self.grid2.add_widget(self.inp1)

        self.grid2.add_widget(UI.Etiquette(text="Prenom", font_size=20, bold=True))
        self.inp2 = TextInput(hint_text="Prenom", font_size=20, multiline=False)
        self.grid2.add_widget(self.inp2)

        self.grid2.add_widget(UI.Etiquette(text="Avatar", font_size=20, bold=True))
        self.layoutImage("crazyfrog.jpg")
        self.layoutImage("diable.jpg")
        self.layoutImage("fallout4.jpg")
        self.layoutImage("gta5.png")
        self.layoutImage("gta5_2.jpg")
        self.layoutImage("hitman2.png")
        self.layoutImage("pomme.png")
        self.layoutImage("smileysourire.png")
        self.grid2.add_widget(self.grid_avatar)


    def layout3(self):
        self.btn = UI.Bouton(text="Enregistrer", font_size=25, color="red", background_color="grey")
        self.btn.bind(on_press=self.clbk_stockcoords)
        self.gridbtn.add_widget(self.btn)

    def layout4(self):
        # Add the contend to the Scroll View
        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.contenu_scroll_grid)

    def layout5(self,utilisateur):
        #Affiche le bouton avec un nom d'utilisateur dans le menu scrollview
        self.btnuser = UI.Bouton(text=utilisateur, font_size=20)
        self.btnuser.bind(on_press=self.clbk_menu_images)
        self.contenu_scroll_grid.add_widget(self.btnuser)

    def layoutImage(self,url):
        #Affiche les avatars (personnages disponibles)
        # Ajout de l'image
        self.img = UI.Bouton(text="",background_normal=url,size_hint=(.1, .3),pos_hint={"x": 0.5, "y": 0.5})
        # centrage de l'image sur l'écran
        self.bind(on_press=self.valider_avatar)
        self.grid_avatar.add_widget(self.img, index=0)

    def popup_window(self):
        self.box = BoxLayout(orientation="vertical")
        self.box.add_widget(UI.Etiquette(text="il faut remplir tous les champs", font_size=17))
        self.btnpop = UI.Bouton(text="Ok", color="red", font_size=15, size_hint=(.35, .35), pos_hint={'center_x': 0.5})
        self.box.add_widget(self.btnpop)
        self.pop = Popup(title="Info", content=self.box, size_hint=(None, None),
                         size=(250, 200), auto_dismiss=False,
                         title_size=30, title_color="green", title_align="center")
        self.btnpop.bind(on_press=self.pop.dismiss)
        self.pop.open()

    def clbk_menu_images(self, widget):
        self.controller.naviguer_menu_map()

    def clbk_stockcoords(self, widget):
        self.controller.stock_coords(self.inp1.text,self.inp2.text, self.img.background_normal)

    def valider_avatar(self,widget,value):
        self.controller.sauvegarder_avatar(self)

class MenuConnexionController():

    def __init__(self, menus):
        self.menus = menus
        self.vue = MenuConnexionVue(self)
        self.lst_noms = []
        self.lst_prenoms = []
        self.lst_avatar = []
        self.personnages = []
        self.avtr = ""
        self.charger_utilisateurs()


    def naviguer_menu_map(self):
        #navuguer vers le menu map
        self.menus.afficher_menu(self.menus.menu_map)

    def charger_list_img(self):
        for src in self.lst_avatar:
            pass

    def charger_utilisateurs(self):
        # ouvrir le fichier user_list et charger les personnages déjà existants
        with  open("user_list.txt","r") as ul:
            lines = ul.readlines()
        for line in lines:
            mot = line.split()
            #charge l'utilisateur par nom prénom avatar
            nom_utilisateur = mot[0] + " | " + mot[1] + " | " + mot[2]
            self.lst_noms.append(mot[0])
            self.lst_prenoms.append(mot[1])
            self.lst_avatar.append(mot[2])
            self.vue.layout5(nom_utilisateur)


    def sauvegarder_avatar(self,value):
        #On stocke le nom de l'avatar dans la variable avtr, déclarée aussi dans la classe vue
        self.avtr = value.img.source
        self.vue.avatar = self.avtr
        Personnage.name_avatar = self.avtr
        print(value.img.background_normal)
        return True

    def enregistrer_vers_map(self,source):
        pass

    def stock_coords(self,nom, prenom,avatar):
        #stocke le nom prenom avatar dans un fichier .txt
        p = Personnage(nom,prenom,avatar)
        print("Utilisateur enregistré : ",nom, prenom,avatar)
        self.personnages.append(p)
        #Enregistre un nouvel utilisateur avec son personnage (avatar) avec sa position par défaut au milieu de l'écran dans le fichier user_list
        if self.vue.inp1.text !="" or self.vue.inp2.text !="":

            with open("user_list.txt", "a") as file:
                file.writelines("{} {} {}\n".format(nom, prenom, avatar))
            new_user = str(nom) +" | "+ str(prenom) + " | " + str(avatar)
            #ajoute le nouvel utilisateur à la liste déjà enregistrée
            self.vue.layout5(new_user)
            self.vue.inp1.text=""
            self.vue.inp2.text=""
            self.avtr=""
            self.naviguer_menu_map()
        else:
            self.vue.popup_window()

            def ecrire_json(x):

                print(x[0])
                g = x[0]
                t = float(x[1])
                ne = int(x[2])
                ad = "user_list.json"
                s = {"Gagne": bool(gagne_perdu(g)), "Duree": round(t, 1), "Nbr essais": ne}

                with open(ad, "w") as mon_fichier:
                    json.dump(s, mon_fichier)
