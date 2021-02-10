index_par_chiffre = {"g": 0, "m": 1, "d": 2 }
index_par_chiffre2 = {"h": 0, "m": 1, "b": 2}
fin = 0

def initialisationtableau():
    taille = 3
    plateau = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append("")
        plateau.append(ligne)
    return plateau
def afficher(tableau):
    
    index = 0
    index_par_lettre = {0: "g", 1: "m", 2: "d"}
    index_par_lettre2= {0: "h", 1: "m", 2: "b"}
    coordonneesX = "  "
    while index < len(tableau):
        coordonneesX = coordonneesX + index_par_lettre[index] + " "
        index = index + 1
    print(coordonneesX)
    print("  _ _ _")
    index = 0
    for ligne in tableau:
        ligne_str = index_par_lettre2[index] + "|"
        for case in ligne:
            ligne_str = ligne_str + case + "|"
        print(ligne_str)
        index = index + 1

def jouer(i):
    if i = 0:
        if fin==0:
            case_valide=1
            while case_valide==1:
                ligne_entree=str(input("Joueur 1, quelle ligne souhaitez-vous? ( h / m / b ) "))
                colonne_entree=str(input("Joueur 1, quelle colonne souhaitez-vous? ( g / m / d ) "))
                coordonnee_x=(index_par_chiffre2[ligne_entree])
                coordonnes_y=(index_par_chiffre[colonne_entree])
                if tableau[coordonnee_x][coordonnee_y]!="":
                    case_valide=0
                    print("Case invalide")
                if case_valide==1:
                    tableau[coordonnee_x][coordonnes_y]="X"
                    afficher(tableau)
                    case_valide=0
        check_victory()
        i=1
    else:
        if fin==0:
            case_valide=1
            while case_valide==1:
                ligne_entree=str(input("Joueur 2, quelle ligne souhaitez-vous? ( h / m / b ) "))
                colonne_entree=str(input("Joueur 2, quelle colonne souhaitez-vous? ( g / m / d ) "))
                coordonnee_x=(index_par_chiffre2[ligne_entree])
                coordonnes_y=(index_par_chiffre[colonne_entree])
                if tableau[coordonnee_x][coordonnee_y]!="":
                    case_valide=0
                    print("Case invalide")
                if case_valide==1:
                    tableau[coordonnee_x][coordonnes_y]="O"
                    afficher(tableau)
                    case_valide=0
        check_victory()
        i = 0

while fin == 0:
    if fin == 0:
        jouer(0)
    if fin == 0:
        jouer(1)
print("Partie terminée")
