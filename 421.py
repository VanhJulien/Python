import random

def victory_check (Nb1, Nb2, Nb3):
    if (Nb1 == "4" and Nb2 == "2" and Nb3 == "1") or (Nb1 == "4" and Nb2 == "1" and Nb3 == "2") or (Nb1 == "2" and Nb2 == "1" and Nb3 == "4") or (Nb1 == "2" and Nb2 == "4" and Nb3 == "1") or (Nb1 == "1" and Nb2 == "4" and Nb3 == "2") or (Nb1 == "1" and Nb2 == "2" and Nb3 == "4"):
        victory_check = 1
        return victory_check
    else:
        victory_check = 0
        return victory_check
        

def roll(d, exception):
    tableau = []
    valeur =""
    if exception == 0:
        for i in range(d):
            lancer = random.randint(1,6)
            tableau.append(lancer)
            valeur = valeur + ", " + str(lancer)
        print (valeur)
        return tableau
    if exception == 1:
        for i in range(d):
            lancer = random.randint(1,6)
            valeur = valeur + str(lancer)
        print (valeur)
        return valeur

def Jeu():
    stock = []
    victory = 0

    
    roll(3, 0)
    garder = (
        input("Que souhaitez-vous garder ? (Entrer pour tout relancer)")
    )
    if len(garder) == 0:
        roll(3, 0)
        garder = (
        input("Que souhaitez-vous garder ? (Entrer pour tout relancer)")
        )
        if len(garder) == 0:
            Nb1 = str(roll(1, 1))
            Nb2 = str(roll(1, 1))
            Nb3 = str(roll(1, 1))
            stock.append(Nb1)
            stock.append(Nb2)
            stock.append(Nb3)
            print(stock)
            victory = victory + victory_check(Nb1, Nb2, Nb3)
            if str(victory) == "1":
                print("Vous avez remporté un point (3 pour gagner)")
            else:
                print("Vous n'avez pas remporté de point, réessayez")
            return victory
        elif len(garder) == 1:
            stock.append(garder)
            
            Nb1 = stock[0]
            Nb2 = str(roll(1, 1))
            Nb3 = str(roll(1, 1))
            stock.append(Nb2)
            stock.append(Nb3)
            print(stock)
            victory = victory + victory_check(Nb1, Nb2, Nb3)
            if str(victory) == "1":
                print("Vous avez remporté un point (3 pour gagner)")
            else:
                print("Vous n'avez pas remporté de point, réessayez")
            return victory
    elif len(garder) == 1:
        stock.append(garder)
        roll(2, 0)
        garder = (
        input("Que souhaitez-vous garder ? (Entrer pour tout relancer)")
        )
        if len(garder) == 0:
            print(stock)
            Nb1 = stock[0]
            Nb2 = str(roll(1, 1))
            Nb3 = str(roll(1, 1))
            stock.append(Nb2)
            stock.append(Nb3)
            print(stock)
            victory = victory + victory_check(Nb1, Nb2, Nb3)
            if str(victory) == "1":
                print("Vous avez remporté un point (3 pour gagner)")
            else:
                print("Vous n'avez pas remporté de point, réessayez")
            return victory
        elif len(garder) == 1:
            stock.append(garder))
            Nb1 = stock[0]
            Nb2 = stock[1]
            Nb3 = str(roll(1, 1))
            stock.append(Nb3)
            print(stock)
            victory = victory + victory_check(Nb1, Nb2, Nb3)
            if str(victory) == "1":
                print("Vous avez remporté un point (3 pour gagner)")
            else:
                print("Vous n'avez pas remporté de point, réessayez")
            return victory

victoire = 0
End = 0
print("--------------------Bienvenue dans le 421 de l'EPSI--------------------")

while victoire < 3 and End != 1:
    play = (
        input ("Souhaitez vous jouer ? (1 pour Oui, autre caractère pour Non)")
    )
    if play == "1":
        victoire = victoire + Jeu()
    else:
        End = 1
    
if victoire == 3:
    print("--------------------Vous avez gagné--------------------")
if End == 1:
    print("--------------------Vous avez perdu, fin du jeu--------------------")
