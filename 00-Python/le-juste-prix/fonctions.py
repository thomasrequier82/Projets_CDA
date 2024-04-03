import csv
import time
import random
import datetime
from CONSTANTE import PRIXDONNE, TEMPSDONNE, T0
import json


def jeudate():
    e = datetime.datetime.now()
    print("Aujourd'hui nous sommes le %s/%s/%s et il est %s:%s:%s"
          % (e.day, e.month, e.year, e.hour, e.minute, e.second))


def tempsdujeu(d):
    diff = d - T0
    return diff


def prix(p):
    n = random.randrange(p[0], p[1])
    return n


# Affiche le jeu du juste prix
def devinez():
    number1 = int(input("Devinez un nombre : "))
    return number1


def justeprix():
    """
            START
    """

    jeudate()
    start = str(input("Bienvenue dans le jeu du juste prix ! (OK POUR COMMENCE LA PARTIE): "))

    while start != "OK":
        start = str(input("Bienvenue dans le jeu du juste prix ! (OK POUR COMMENCER LA PARTIE): "))

        print("Bonne chance !")

    """
            JEUX
    """
    number = prix(PRIXDONNE)
    number1 = 0
    nombreessais = 0
    gagne = "Gagné"
    perdu = "Perdu"
    print(number)

    while number != number1:
        temp = time.time()
        tempsrestant = float(round(TEMPSDONNE - (tempsdujeu(temp)), 1))
        if tempsdujeu(temp) < TEMPSDONNE:
            number1 = devinez()
            if number < number1:
                print("Plus petit !")
                print("Temps restant : ", tempsrestant, "secondes")
                nombreessais += 1
            if number > number1:
                print("Plus grand !")
                print("Temps restant : ", tempsrestant, "secondes")
                nombreessais += 1
            if number == number1:
                nombreessais += 1
                return gagne, tempsrestant, nombreessais
        else:
            return perdu, tempsrestant, nombreessais

def gagne_perdu(jeu):
    if jeu == "Perdu":
        return False
    elif jeu == "Gagné":
        return True

def affichage(afficher):
    affich = afficher
    print("Vous avez %s en %s secondes" % (afficher[0], afficher[1]))
    return affich


def ecrirefichiertexte(resultat):
    etat = str(resultat[0])
    tempspartie = str(resultat[1])
    nbessai = str(resultat[2])
    fichier = open("lejusteprix.txt", "w")
    score = "%s; %s s; %s essais\n" % (etat, tempspartie, nbessai)
    fichier.write(score)
    fichier.write("#######################")
    fichier.close()


def ecrirefichiercsv(resultat):
    with open('lejusteprix.csv', 'w') as fichier_csv:
        etat = str(resultat[0])
        tempspartie = str(resultat[1])
        nbessai = str(resultat[2]) + " essais"
        fin = "\n#######################"
        writer = csv.writer(fichier_csv, lineterminator='\n', delimiter=";")
        score = [etat, tempspartie, nbessai, fin]
        writer.writerow(score)


def afficherfichier(fichier: str):
    with open(fichier) as fichier:
        for ligne in fichier:
            print(ligne)


def ecrire_json(x):

    print(x[0])
    g = x[0]
    t = float(x[1])
    ne = int(x[2])
    ad = "juste_prix.json"
    s = {"Gagne": bool(gagne_perdu(g)), "Duree": round(t, 1), "Nbr essais": ne}

    with open(ad, "w") as mon_fichier:
        json.dump(s, mon_fichier)
