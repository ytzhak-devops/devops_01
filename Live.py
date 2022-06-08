def welcome(name):
    username = input('Please enter your name: ')
    print(f"Hello {username} and welcome to the World of Games(WoG)\
          \nHere you can find many cool games to play.")


welcome("username")


def load_game():
    choice = input("""
    Please choose a game to play:
    
    1. Memory Game        - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game         - guess a number and see if you chose like the computer
    3. Currency Roulette  - try and guess the value of a random amount of USD in ILS
    
    make a selection : 
    """)

    if 1 <= choice.isdigit() <= 3:
        difficulty = input('Please choose game difficulty from 1 to 5 : ')
        if 1 <= difficulty.isdigit() <= 5:
            print(f'You choose {difficulty} level , good luck...')
        else:
             print("Not a valid number ! Try again...")
    else:
        print("Not a valid number ! Try again...")

load_game()

