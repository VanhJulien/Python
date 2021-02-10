import random
import emojis





def CreateLine():
    i = 0
    ligne = []
    for i in range(5):
        emoji = random.randint(1, 4)
        ligne.append(str(emoji))
        i = i+1

    return ligne

def afficher_board (plateau):
    for ligne in plateau:
        ligne_str = ""
        for case in ligne:
            ligne_str = ligne_str + case + " "
        print(ligne_str)

def MachineASous():
    board =[]
    for loop in range (5):
        board.append(CreateLine())


    board2 =[]
    for loop in range (5):
        board2.append(CreateLine())
    

    boards = [board, board2]


    victoire = False
    while victoire is False:
        for w in range(len(boards)):
            print("------------------------------------------- Joueur numéro : " + str(w) +" -------------------------------------------\n")
            afficher_board(boards[w])
            if w == 0:
                garder = (
                    input("Saisissez le fruit à garder, 1 pour 1, 2 pour 2, 3 pour 3, 4 pour 4 : "))
                print("\n")
                for I in range (0,5):
                    for J in range (0,5):
                        if boards[w][I][J] != garder :
                            boards[w][I][J] = str(random.randint(1,4))
                
            else : 
                IA = 0
                for ligne in boards[w]:
                    onecount = 0
                    twocount = 0
                    threecount = 0
                    fourcount = 0
                    for case in ligne:
                        if onecount == "1":
                            onecount = onecount + 1                  
                        elif twocount == "2":
                            twocount = twocount + 1
                        elif threecount == "3":
                            threecount = threecount + 1
                        elif fourcount == "4":
                            fourcount = fourcount + 1    
                    if onecount >= twocount and onecount >= threecount and onecount >= fourcount:
                        IA = "1"
                    if twocount >= onecount and twocount >= threecount and twocount >= fourcount:
                        IA = "2"
                    if threecount >= onecount and threecount >= twocount and threecount >= fourcount:
                        IA = "3"
                    if fourcount >= onecount and fourcount >= twocount and fourcount >= threecount:
                        IA = "4"
                print("Le joueur 1 a choisi de garder les " + IA + "\n")
                garder= (IA)
                for I in range (0,5):
                    for J in range (0,5):
                        if boards[w][I][J] != garder :
                            boards[w][I][J] = str (random.randint(1,4))
                

            



            for ligne in boards[w]:
                save=""
                check=0
                for case in ligne:
                    if save=="":
                        save = case
                        check = check + 1
                    elif save == case:
                        save = case
                        check = check + 1
                if check == 5:
                    victoire=True
                    print("Bravo, le joueur " + str(w) + " a remporté la partie.\n") 
            
End = False
while End is False:
    MachineASous()
    Replay = (
        input("\n Saisissez n'importe quel caractère pour rejouer ou 0 pour arrêter \n")  
    )
    if Replay == "0" :
        End = True

