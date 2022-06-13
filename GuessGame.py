# guess game

import random

difficulty = True
while difficulty:
    upper_number = input('Enter the upper number : ')
    if upper_number.isdigit():
        print("Let's Play ! ")
        upper_number = int(upper_number)
        difficulty = False
    else:
        print("Invalid input! Try again... ")

secret_number = random.randint(1, upper_number)

guess = None
count = 1

while guess != secret_number:
    guess = input("Please type a number between 1 and " + str(upper_number) + ":" )
    
        
              
    if guess.isdigit():
        guess = int(guess)
    if guess == secret_number:
        print("You got it ! ")
    else:
        print("Please try again ...")
        count += 1
        
print("It took " , count , "guesses ", "Goodbye...")

      


            
