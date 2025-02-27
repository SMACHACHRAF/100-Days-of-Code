niveau_jeu = 10
ennemis = ["Squelette", "Zombie", "Extraterrestre"]

def creer_ennemi():
    nouvel_ennemi = ""
    if niveau_jeu < 5:
        nouvel_ennemi = ennemis[0]
    print(nouvel_ennemi)

creer_ennemi()
