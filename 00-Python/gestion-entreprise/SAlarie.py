from Personne import Personne
import random

class Salarie():
    SALARIES = []
    def __init__(self, **attributes):
        [setattr(self, k, v) for k, v in attributes.items()]

    def changer_salaire(self, valeur,dir):
        if isinstance(dir,Directeur):
            dir.augmenter_salaire(valeur,self)
        else:
            raise AccessRightError("Il n'y a que le directeur qui puisse changer le salaire !")

    def afficher_infos(self):
        print("Je m'appelle ", self.prenom, " et je gagne ", self.salaire, " par mois.")

    @classmethod
    def initEmployes(cls):
        #Initialisation des Salariés entre 30 et 150 aléatoirement
        for i in range(random.randrange(30,150)):
            cls.creersalarie(entreprise = random.choice(seq=[0,1,None]))

    @classmethod
    def creersalarie(cls, entreprise = None):
        voitures = random.randrange(0, 5)
        if voitures == 0:
            attrs = {"entreprise": entreprise, "salaire": random.randrange(1200, 2000),
                     "voitureFonction": True, "Voiture": voitures,"efficacite":random.randrange(1,50) / 1000,"tempsentreprise":0}
        else:
            attrs = {"entreprise": entreprise, "salaire": random.randrange(1200, 2000),
                     "voitureFonction": random.choice(seq=[True, False]), "Voiture": voitures, "efficacite":random.randrange(1,50) / 1000,"tempsentreprise":0}
        salarie = Salarie(**attrs)
        cls.SALARIES.append(salarie)

    def changeAttr(self,attr: str,value):

        self.__setattr__(attr,value)

class Directeur(Salarie):
    def __init__(self,**attributes):
        super().__init__(**attributes)

    def augmenter_salaire(self, valeur,salarie):
        salarie.salaire += valeur

class AccessRightError(Exception):
    def __init__(self,msg="Exception: Seul le directeur peut augmenter un salarié !"):
        super().__init__(msg)
    pass