import getpass


word = getpass.getpass()
essais = ''
print("Début du jeu...")

turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in essais:
            print(char,)
        else:
            print("_",)
            failed += 1

    if failed == 0:
        print("Vous avez gagné")
        break

    
    essai = input("Devinez une lettre:")
    essais += essai
    if essai not in word:
        turns -= 1
        print("Faux")
        print("Vous avez", + turns, 'essais restants')

if turns == 0:
    print("Vous avez perdu")