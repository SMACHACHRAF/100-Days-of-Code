enemies = 1

def augmenter_enemis():
    enemies = 2
    print(f"enemies inside function: {enemies}")

augmenter_enemis()
print(f"enemies outside function: {enemies}")
def boire_potion():
    potion_force = 2
    print(potion_force)
boire_potion()
sante_joueur = 10
def jeu():
    def boire_potion():
        potion_force = 2
        print(sante_joueur)
    boire_potion()

print(sante_joueur)
