from random import randint

FACILE = 10
DIFFICILE = 5


def verifier_reponse(supposition, reponse, tentatives):
    if supposition > reponse:
        print("Trop haut.")
        return tentatives - 1
    elif supposition < reponse:
        print("Trop bas.")
        return tentatives - 1
    else:
        print(f"Bravo ! La réponse était {reponse}")


def choisir_difficulte():
    niveau = input("Choisissez une difficulté : 'facile' ou 'difficile' : ")
    return FACILE if niveau == "facile" else DIFFICILE


def jeu():
    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100.")
    reponse = randint(1, 100)
    print(f"(Indice : la réponse est {reponse})")

    tentatives = choisir_difficulte()
    supposition = 0

    while supposition != reponse:
        print(f"Il vous reste {tentatives} tentative(s).")
        supposition = int(input("Faites une supposition : "))
        tentatives = verifier_reponse(supposition, reponse, tentatives)
        if tentatives == 0:
            print("Vous avez épuisé toutes vos tentatives. Vous avez perdu.")
            return
        elif supposition != reponse:
            print("Essayez encore.")


jeu()
