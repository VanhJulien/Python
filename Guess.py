import random

def evaluate(guess_number, secret_number):
    found = False
    if guess_number < secret_number:
        print('Higher!')
    elif guess_number > secret_number:
        print('Lower!')
    else:
        found = True
    return found
    
# Guess the number
print('== Guess the number ==')
secret_number = random.randint(1, 100)
guess_number = None
while guess_number != secret_number:
    try:
        guess_number = int(input())
        found = evaluate(guess_number, secret_number)
    except ValueError:
        print('You must enter a number to play our guessing number game')

print(f'Found! The secret number was {secret_number}')