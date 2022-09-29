import random

chiffre_aleatoire = random.randint(1, 1000)
nbrEssaie = 10


while nbrEssaie != 0:
    essaie = input("\n choisis un nombre entre 1 et 1000 tu a %d essaie:"%(nbrEssaie))

    if essaie > chiffre_aleatoire:
        print("Le nombre mystère est plus petit")

    elif essaie < chiffre_aleatoire:
        print("Le nombre mystère est plus grand")

    elif essaie == chiffre_aleatoire:
        print("Tu as trouvé le nombre mystère bravo")
        break

    if essaie != chiffre_aleatoire :
        nbrEssaie = nbrEssaie-1

    elif nbrEssaie == 0:
        print("tu n'as pas réussie a trouver le nombre %d,tu as perdu."%(chiffre_aleatoire))