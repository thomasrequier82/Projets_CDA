import random
from entreprise import Entreprise
from SAlarie import *
import matplotlib
from graph import Graph
import constantes as C
#from export import exportDonnees


"""class Simulation():
    def __init__(self):
        self.chef = None
        self.entreprise = None
        self.liste_personnes = []

    def jeu_donnees_1(self):
        self.chef = Salarie.Directeur("toto", 3)
        self.entreprise = Entreprise.Entreprise(self.chef)
        self.liste_personnes = [Salarie("antoine", 1), Salarie("Nicolas", 2)]

    def jeu_donnees_2(self):
        self.chef = Salarie.Directeur("zorro", 1)
        self.entreprise = Entreprise.Entreprise(self.chef)
        self.liste_personnes = [Salarie.Salarie("pierre", 2), Salarie.Salarie("jean", 3)]

    def animer(self):
        self.entreprise.embaucher(self.liste_personnes[0])
        self.entreprise.afficher_salaries()"""

def main():
    moiscomparaison(C.MOIS_MAX)
    Salarie.initEmployes()
    Entreprise.creerEntreprise()
    mois = 0
    #Graph.initGraph()
    while mois < C.MOIS_MAX:
        print("Mois", mois+1," :")
        for e in Entreprise.ENTREPRISES:
            nouvSalaries =random.randrange(10)
            for i in range(nouvSalaries):
                Salarie.creersalarie(None)
            e.mise_jour_mensuelle()
            print("Mois de  ",mois," :",end=" ")
            print("Employés:", len(e.salaries))
        mois += 1
    args = {"title": "Revenus des Entreprises","xName": "Mois","yName":"Euros"}
    #exportDonnees.exportCsv()
    #exportDonnees.exportJson()
    graph = Graph(**args)
    graph.showGraph()

class PeriodOutOfScopeError(Exception):
    """
        Nombre de mois négatifs ou supérieur à 120
    """
    def __init__(self,msg="Exception: Nbr mois négatif ou supérieurs à 120"):
        super().__init__(msg)

class NumberFormatException(Exception):
    def __init__(self, message, value):
        message = f'{value} is not a number'
        super().__init__(message)


def moiscomparaison(mois):
    message ="Exception occured"
    if type(mois) == str:
        raise NumberFormatException(message, mois)
    elif mois <=0 or mois > 120:
        raise PeriodOutOfScopeError()
    else:
        return mois

if __name__ == "__main__":
    main()
    """ print("### SIMULATION 1 ####")
    simulation1 = Simulation()
    simulation1.jeu_donnees_1()
    simulation1.animer()
    print("\n###### SIMULATION 2 #####")
    simulation2 = Simulation()
    simulation2.jeu_donnees_2()
    simulation2.animer()"""

