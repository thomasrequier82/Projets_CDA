from fonctions import affichage, ecrirefichiertexte, ecrirefichiercsv, afficherfichier, ecrire_json, justeprix


def main():
    print("### JEU DU JUSTE PRIX ###")
    resultat = affichage(justeprix())
    ecrirefichiertexte(resultat)
    ecrirefichiercsv(resultat)
    ecrire_json(resultat)

    print("### Afficher le contenu des fichiers ###")
    print("Txt :")
    afficherfichier("lejusteprix.txt")
    print("CSV :")
    afficherfichier("lejusteprix.csv")
    print("Json :")
    afficherfichier("juste_prix.json")

main()
