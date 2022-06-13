# guess game

import random

difficulty = True
while difficulty:
    bom = input('Enter your difficulty level : ')
    if bom.isdigit():
        print("Let's Play ! ")
        bom = int(bom)
        difficulty = False
    else:
        print("Invalid input! Try again... ")

secret_number = random.randint(1, bom)

guess = None
count = 1

while guess != secret_number:
    guess = input("Please type a number between 1 and " + str(bom) + ":" )
    
        
              
    if guess.isdigit():
        guess = int(guess)
    if guess == secret_number:
        print("You got it ! ")
    else:
        print("Please try again ...")
        count += 1
        
print("It took " , count , "guesses ", "Goodbye...")

