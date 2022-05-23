# Plateau de 10x10 contre l'IA
# Les colonnes numérotées entre A-J, les lignes 0-9
# On place aléatoire les bateaux de taille (une taille de 5, une taille de 4, deux taille de 3, une taille de 2 et une taille de 1)
# On demande le ou le joueur souhaite tiré (A9)
# S'il touche, on marque la case
# S'il rate, on le notifie
# A chaque tour on lui montre son plateau
# Le vainqueur quand il n'y a pu de bateau !
# Un tableau de 10x10
# Placer des bateaux dessus (6, de taille 5,4, 2*3, 2 , 1)
# Tu prends une case au hasard, tu prend une orientation au hasard, taille -> Si ça sort tu recommences, sinon tu places

import random
i=0
j=0
fin=0
check=1
check2=1
direction_bateau= {0: "d", 1: "b", 2: "g", 3: "h"}
index_par_chiffre = {"A": 0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
def initialisation_tableau():
    taille = 10
    plateau = []
    for x in range(taille):
        ligne = []
        for y in range(taille):
            ligne.append("~")
        plateau.append(ligne)
    return plateau

def afficher(tableau):
    index = 0
    index_par_letter = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
    coordonneesX = "  "
    while index < len(tableau):
        coordonneesX = coordonneesX + index_par_letter[index] + " "
        index = index + 1
    print(coordonneesX)
    index = 0
    for ligne in tableau:
        ligne_str = str(index) + " "
        for col in ligne:
            ligne_str = ligne_str + col + " "
        print(ligne_str)
        index = index + 1

def placement_bateau(taille):
    continuer=1
    while continuer==1:
        in_range=1
        while in_range == 1 :
            x=1
            i=random.randint(0,9)
            j=random.randint(0,9)
            direction_chiffre=random.randint(0,3)
            direction=direction_bateau[direction_chiffre]
            if direction == "d":
                if j+taille<10 and j+taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau[i][j + x] == "b":
                            in_range=1
            if direction == "b":
                if i+taille<10 and i+taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau[i + x][j] == "b":
                            in_range=1
            if direction == "g":
                if j-taille<10 and j-taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau[i][j - x] == "b":
                            in_range=1
            if direction == "h":
                if i-taille<10 and i-taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau[i - x][j] == "b":
                            in_range = 1
            if in_range == 0:
                tableau[i][j] = "b"
                if direction == "d" :
                    for x in range (taille):
                        tableau[i][j+x]="b"
                if direction == "b" :
                    for x in range (taille):
                        tableau[i+x][j]="b"
                if direction == "g" :
                    for x in range (taille):
                        tableau[i][j-x]="b"
                if direction == "h" :
                    for x in range (taille):
                        tableau[i-x][j]="b"
                continuer=0

def placement_bateau_adverse(taille):
    continuer=1
    while continuer==1:
        in_range=1
        while in_range == 1 :
            x=1
            i=random.randint(0,9)
            j=random.randint(0,9)
            direction_chiffre=random.randint(0,3)
            direction=direction_bateau[direction_chiffre]
            if direction == "d":
                if j+taille<10 and j+taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau2[i][j + x] == "b":
                            in_range=1
            if direction == "b":
                if i+taille<10 and i+taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau2[i + x][j] == "b":
                            in_range=1
            if direction == "g":
                if j-taille<10 and j-taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau2[i][j - x] == "b":
                            in_range=1
            if direction == "h":
                if i-taille<10 and i-taille>=0:
                    in_range = 0
                    for x in range(taille):
                        if tableau2[i - x][j] == "b":
                            in_range = 1
            if in_range == 0:
                tableau2[i][j] = "b"
                if direction == "d" :
                    for x in range (taille):
                        tableau2[i][j+x]="b"
                if direction == "b" :
                    for x in range (taille):
                        tableau2[i+x][j]="b"
                if direction == "g" :
                    for x in range (taille):
                        tableau2[i][j-x]="b"
                if direction == "h" :
                    for x in range (taille):
                        tableau2[i-x][j]="b"
                continuer=0

print("Bienvenue au jeu de la bataille navale. Objectif: Battre l'IA ! ")


tableau = initialisation_tableau()
placement_bateau(5)
placement_bateau(4)
placement_bateau(3)
placement_bateau(3)
placement_bateau(2)
placement_bateau(1)
tableau2 = initialisation_tableau()
placement_bateau_adverse(5)
placement_bateau_adverse(4)
placement_bateau_adverse(3)
placement_bateau_adverse(3)
placement_bateau_adverse(2)
placement_bateau_adverse(1)
tableau3 = initialisation_tableau()
def afficher_planche():
    print("Votre planche avec vos navires.")
    afficher(tableau)
    print("Planche adversaire.")
    afficher(tableau3)

def tir_allier():
    a = str(input("Entrez l'abscisse de la case où vous souhaitez effectuer votre tir."))
    b = int(input("Entrez l'ordonnée de la case où vous voulez effectuer votre tir."))
    c = int(index_par_chiffre[a])
    if (tableau2[b][c])=="b":
        tableau3[b][c]="X"
        tableau2[b][c] = "X"
        print("Vous avez touché un navire adverse !")
    if  (tableau2[b][c])=="~":
        tableau3[b][c]="0"
        print("Vous avez tiré... Dans l'eau !")

def tir_adverse():
    b = random.randint(0,9)
    c = random.randint(0,9)
    if (tableau[b][c])=="b":
        tableau[b][c]="X"
        print("L'adversaire a touché un de vos navires. Ne perdez pas courage !")
    if  (tableau[b][c])=="~":
        tableau[b][c]="0"
        print("L'adversaire a loupé ! A vous d'attaquer ")

def check_victoire():
    check=0
    check2=0
    fin=0
    for i in range(10):
        for j in range (10):
            if tableau[i][j]=="b":
                check2=check2+1
    if check2  < 1:
        fin = 2
    for k in range (10):
        for l in range (10):
            if tableau2[k][l]=="b":
                check=check+1
    if check < 1:
        fin = 1
        print("gagné")
afficher_planche()
fin=0
while fin==0:
    if fin==0 :
        check=0
        check2=0
        tir_allier()
        tir_adverse()
        afficher_planche()
        check_victoire()
if fin==1:
    print("La partie est terminée, le joueur victorieux est ",fin)

