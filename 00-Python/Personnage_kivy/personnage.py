
class Personnage():
    def __init__(self, nom, prenom,avatar):
        self.position = {'center_x': 0.5, 'center_y': 0.5}
        self.nom = nom
        self.prenom = prenom
        self.name_avatar = avatar

    def Position(self):
        return self.position