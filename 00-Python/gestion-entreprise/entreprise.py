import SAlarie
from Voiture import *
from SAlarie import Salarie, Directeur
from Bureau import *
import random

class Entreprise():
    """Crée une Entreprise"""
    ENTREPRISES = []

    def __init__(self, i):
        self.id = 0
        self.chargesMois = 0
        self.gainMois = 0
        self.CAmensuel = random.randrange(50000,200000)
        self.Fonds = random.randrange(1000000,3000000)
        self.directeur = self.nouvDirecteur()
        self.salaries = []
        self.voituresFonction = []
        self.bureaux = []
        self.mois = []
        self.historiquemois = []
        self.historiquechargesmois = []
        self.historiquegainmois = []
        self.historiquevoituresmois = []
        self.historiquesalariemois = []
        self.historiquebureauxmois = []

        self.graph = None

        self.embaucherEmployes()
        self.achatVoituresFonction()
        #self.achatBureaux()
        self.directeur = self.nouvDirecteur()

    def mise_jour_mensuelle(self):
        print("Fonds =",self.Fonds, end=", ")
        self.chargesMois += self.chargesMensuelle()
        self.gainMois += self.beneficeMensuel()
        self.turnoverSalaries()
        self.Fonds = self.gainMois - self.chargesMois
        self.historiquemois.append(self.Fonds)
        self.historiquevoituresmois.append(len(self.voituresFonction))
        self.historiquesalariemois.append(len(self.salaries))
        self.historiquebureauxmois.append(len(self.bureaux))

        print("Charges mensuelles =",self.chargesMois, end=", ")
        print("Chiffre d'affaires Mensuel =", self.CAmensuel, end=", ")
        print("Fonds = ", self.Fonds)
        self.historiquechargesmois.append(self.chargesMois)
        self.historiquegainmois.append(self.gainMois)
        self.chargesMois = 0
        self.gainMois = 0
        n = 0
        for s in Salarie.SALARIES:
            if s.entreprise is None:
                n += 1
            elif s.entreprise is self:
                s.changeAttr("tempsentreprise", s.tempsentreprise + 1)
                if random.randrange(100) + s.tempsentreprise >= 50:
                    s.changeAttr("efficacite",random.randrange(1,10)/1000)
        print(n,"Salariés sans emploi")



    def turnoverSalaries(self):
        """sM = StartMoney eM = EndMoney"""
        ns = 0
        nVoiture = 0
        nBureau = 0
        #Situation critique: On perd de l'argent, on vire !!
        if self.chargesMois > self.gainMois or self.Fonds + self.gainMois - self.chargesMois < 0:
            while (self.chargesMois > self.gainMois or self.Fonds + self.gainMois - self.chargesMois < 0) and \
                    len(self.historiquemois) >= 1:
                if len(self.salaries) <= 1:
                    break
                salarie = self.salaries[0]
                for s in self.salaries:
                    if s.salaire > salarie.salaire or (s.tempsentreprise < salarie.tempsentreprise and s.efficacite > salarie.efficacite):
                        salarie = s
                if salarie.voitureFonction:
                    for voit in self.voituresFonction:
                        if voit .salarie == salarie:
                            self.vendreVoitureFonction(voit)
                            nVoiture += 1
                            break
                ns += 1
                self.virerEmploye(salarie, avecBureau=True)

            print("A Viré",ns,"Salariés, et vendu ",ns," Bureaux et ",nVoiture," voitures de fonction")

        #Situation Satisfaisante: On gagne de l'argent, on peut embauchere !!
        elif self.chargesMois < self.gainMois:
            oldS = 0
            while self.chargesMois < self.gainMois or self.Fonds + self.gainMois - self.chargesMois < 0:
                for s in Salarie.SALARIES:
                    if self.chargesMois < self.gainMois or self.Fonds + self.gainMois - self.chargesMois < 0:
                        break
                    if s.entreprise is None:
                        if self.gainMois + s.salaire - self.CAmensuel*s.efficacite > self.gainMois or self.Fonds - self.chargesMois + self.gainMois - s.salaire - self.CAmensuel * s.efficacite < 0:
                            continue
                        if len(self.bureaux) > len(self.salaries):
                            self.embaucherEmploye(s)
                        else:
                            self.embaucherEmploye(s, avecBureau=True)
                            nBureau += 1
                        if s.voitures == 0 and len(self.voituresFonction) < len(self.salaries):
                            s.changeAttr("voitureFonction",True)
                            self.achatVoitureFonction(s)
                            nVoiture +=1
                        ns +=1
                if oldS == ns:
                    break
                oldS = ns

            print("A embauché ",ns," salairiés et acheté ", nBureau," bureaux et ",nVoiture," Voitures de fonction")

    def chargesMensuelle(self):
        for s in self.salaries:
            self.chargesMois += s.salaire
        self.chargesMois += self.directeur.salaire
        for vehicule in self.voituresFonction:
            self.chargesMois += vehicule.cout_mensuel
        return self.chargesMois

    def beneficeMensuel(self):
        total = self.CAmensuel
        for s in self.salaries:
            total += self.CAmensuel * s.efficacite
         #self.CAmensuel = random.randrange(35000,9000)
        #self.gainMois = self.CAmensuel
        return int(total)

    @classmethod
    def creerEntreprise(cls):
        """Créer deux entreprises"""
        for i in range(2):
            entreprise = Entreprise(i)
            cls.ENTREPRISES.append(entreprise)

    def nouvDirecteur(self):
        return SAlarie.Directeur(**{"entreprise": random.choice(seq=[0,1,None]), "salaire": random.randrange(1200, 2000),
                         "voitureFonction": True, "Voiture":random.randrange(0,7)})

    def embaucherEmployes(self):
        for s in Salarie.SALARIES:
            if s.entreprise == self.id:
                self.embaucherEmploye(s)

    def embaucherEmploye(self, salarie: Salarie, avecBureau=False):
        prix = 0
        sPourcentage = 0
        salarie.changeAttr("entreprise",self)
        if salarie not in self.salaries:
            self.salaries.append(salarie)
            sPourcentage = self.CAmensuel * salarie.efficacite
            prix += salarie.salaire

            if avecBureau:
                bureau = self.achatBureau(salarie)
                prix += bureau.prix
        self.gainMois = int(sPourcentage)
        self.chargesMois = prix
        print("Bienvenue !")


    def virerEmploye(self, salar,avecBureau=False):
        if salar in self.salaries:
            self.salaries.remove(salar)
            salar.changeAttr("tempsentreprise",0)
            for b in self.bureaux:
                if b.salarie is not None and b.salarie == salar:
                    b.changeAttr("salarie",None)
                    if avecBureau:
                        self.vendreBureau(b)
                break
            salar.changeAttr("entreprise",None)
            if salar.voitureFonction:
                salar.changeAttr('voitureFonction',False)
            self.gainMois -= int(self.CAmensuel*salar.efficacite)

        #self.salaries.remove(salar)

        print("Aurevoir !")

    def achatVoituresFonction(self):
        """Achète toutes les voitures de fonction de l'entreprise"""
        [self.achatVoitureFonction(e) for e in self.salaries]

    #@staticmethod
    def achatVoitureFonction(self, salar):
        """Achat de voiture de fonction (entreprise, salarié)"""
        if salar.voitureFonction:
            attrs = {"entreprise": self, "salarie":salar}
        else:
            if salar.Voiture == 0:
                salar.voitureFonction = True
                attrs = {"entreprise": self, "salarie":salar}
            else:
                attrs = {"entreprise": self, "salarie":None}
        if attrs["salarie"] is None:
            return None
        attrs["prix"] = random.randrange(25000,75000)
        attrs["cout_mensuel"] = random.randrange(50,500)
        voiture = VoitureFonction(**attrs)
        #oitureFonction.VOITURESFONCTION.append(voiture)
        self.voituresFonction.append(voiture)
        self.chargesMois += voiture.prix

    def vendreVoitureFonction(self,voiture):
        self.gainMois += voiture.prix
        voiture.changeAttr("salarie",None)
        self.voituresFonction.remove(voiture)

    #@staticmethod
    def achatBureaux(self):
        [self.achatBureaux(s) for s in self.salaries]


    def achatBureau(self,employe):
        attrs = {
            "salarie":employe,
            "prix": random.randrange(250,1500)
        }
        bureau = Bureau(**attrs)
        self.bureaux.append(bureau)
        #Bureau.BUREAUX.append(bureau)
        self.chargesMois += bureau.prix
        return bureau

    def vendreBureau(self,bureau):
        self.gainMois += bureau.prix
        bureau.changeAttr("salarie",None)
        #Bureau.BUREAUX.remove(bureau)
        self.bureaux.remove(bureau)


    def afficher_salaries(self):
        for salarie in self.salaries:
            salarie.afficher_infos()
