# crée par mathis robinet
# crée le 22-09-26
# TP2
import random
rejouer = input(str("veux-tu faire une partie \n oui , non: "))

while rejouer =="oui":
    print("Le jeu de la devinette:")
    regle = input(str("Veux-tu savoir les règles du jeu \n oui , non: "))

    if regle == ("oui"):
        print("Les règles du jeu de la devinette: "
              "\n un nombre entier aléatoire est choisis entre 1 et 1000 et tu dois le deviner. "
              "\n À chaque erreur il y est afficher si le nombre écris est plus petit , plus grand ou égale que le nombre mystère. "
              "\n Plus tu fais d'erreur plus ton nombre d'essaie diminue et tu as 10 essaie")

    chiffre_aleatoire = random.randint(1, 1000)
    nbrEssaie = 11

    while nbrEssaie != 0:
        essaie = input("\n écris un nombre entier entre 1 et 1000 tu a %d essaie: "%(nbrEssaie))
        essaieINT = int(essaie)

        if essaieINT > chiffre_aleatoire:
            print("Le nombre mystère est plus petit")

        elif essaieINT < chiffre_aleatoire:
            print("Le nombre mystère est plus grand")

        elif essaieINT == chiffre_aleatoire:
            #print("Tu as trouvé le nombre mystère bravo\n")
            for i in range(50):
                print(i * " " + "Bravo vous avez trouvé le nombre mystère.")
            break

        if essaieINT != chiffre_aleatoire :
            nbrEssaie = nbrEssaie-1

        if nbrEssaie == 0:
            print("tu n'as pas réussie a trouver le nombre %d,tu as perdu."%(chiffre_aleatoire))

    rejouer = input(str("veux-tu refaire un partie \n oui , non: "))






