from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Ecran(BoxLayout):
    def build(self):
        self.orientation = 'vertical'
        self.spacing = 20
        self.Mes_Boutons()

    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Liste_Boutons = []
        # On fait tourner une boucle pour creer 10 boutons:
        for i in range(0, 10):
            # On ajoute un bouton dans la liste:
            self.Liste_Boutons.append(Button())
            # On lui donne un texte qui depend de i:
            self.Liste_Boutons[i].text = "Bouton " + str(i)
            # On lui donne un identite "id" pour le retrouver hors de la liste:
            self.Liste_Boutons[i].id = "B" + str(i)
            # On lui associe une fonction:
            self.Liste_Boutons[i].bind(on_press=self.Une_Fonction_Bouton)
            # On ajoute le bouton au layout principal:
            self.add_widget(self.Liste_Boutons[i])

        # On ajoute une couleur de fond au dernier bouton:
        self.Liste_Boutons[9].background_color = [0, 1, 0, 1]

    def Une_Fonction_Bouton(self, instance):
        # instance correspond au bouton qui vient d'etre active:
        # On change la couleur des neuf premiers boutons:
        for i in range(0, 9):
            self.Liste_Boutons[i].background_color = [0.5, 0.5, 0.5, 1]  # En gris
        # On change la couleur du bouton active si ce n'est pas le dernier:
        if instance.id != "B9":
            instance.background_color = [1, 0, 0, 1]  # En rouge


class BoutonsApp(App):

    def build(self):
        root = Ecran()
        root.build()
        return root

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(BoxLayout):
    def __init__(self,parent,**kwargs):
        BoxLayout.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def main():
    root = Ecran()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="red", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    mycanvas.create_line(0, 0, 200, 100)
    mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()

#if __name__ == '__main__':
    BoutonsApp().run()