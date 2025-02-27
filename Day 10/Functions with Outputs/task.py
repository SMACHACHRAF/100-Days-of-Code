# ✅ Fonction qui formate le prénom et le nom en Title Case
def formater_nom(prenom, nom_de_famille):
    prenom_formate = prenom.title()        # Met la première lettre en majuscule
    nom_formate = nom_de_famille.title()   # Idem pour le nom
    return f"{prenom_formate} {nom_formate}"  # Retourne le nom complet formaté


# 🖨️ Exemple d'appel de la fonction
nom_complet = formater_nom("AnGeLa", "YU")
print(nom_complet)  # Résultat attendu : Angela Yu


# ✅ Fonction qui répète un texte deux fois
def repeter_texte(texte):
    return texte * 2   # Multiplie la chaîne par 2 (texte + texte)


# ✅ Fonction qui met un texte en Title Case (majuscule sur chaque mot)
def mettre_en_majuscule(texte):
    return texte.title()


# 🔗 Combinaison des deux fonctions : répéter puis formater
texte_final = mettre_en_majuscule(repeter_texte("hello "))
print(texte_final)  # Résultat attendu : Hello Hello
