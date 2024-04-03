class Voiture():
    VOITURES = []

    def __init__(self, **attributes):
        [setattr(self, k, v) for k, v in attributes.items()]

    def changeAttr(self,attr: str,value):

        self.__setattr__(attr,value)

class VoitureFonction(Voiture):
    VOITURESFONCTION = []

    def __init__(self, **attributes):
        super().__init__(**attributes)


class VoiturePerso(Voiture):
    VOITURESPERSO = []

    def __init__(self, **attributes):
        super().__init__(**attributes)