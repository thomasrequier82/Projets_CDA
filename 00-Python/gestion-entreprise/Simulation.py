class Simulation():
    def __init__(self):
        self.VOITURES = []
        self.SALARIES = []
        self.BUREAUX = []
        self.chef = None
        self.entreprise = None


    def jeu_donnees_1(self):
        self.chef = Salarie.Directeur("toto", 3)
        self.entreprise = Entreprise.Entreprise(self.chef)
        self.liste_personnes = [Salarie("antoine", 1), Salarie("Nicolas", 2)]

    def jeu_donnees_2(self):
        self.chef = Salarie.Directeur("zorro", 1)
        self.entreprise = Entreprise.Entreprise(self.chef)
        self.liste_personnes = [Salarie.Salarie("pierre", 2), Salarie.Salarie("jean", 3)]

    def moiscomparaison(mois):
        message = "Exception occured"
        if type(mois) == str:
            raise NumberFormatException(message, mois)
        elif mois <= 0 or mois > 120:
            raise PeriodOutOfScopeError()
        else:
            return mois

    def animer(self):
        self.entreprise.embaucher(self.liste_personnes[0])
        self.entreprise.afficher_salaries()

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