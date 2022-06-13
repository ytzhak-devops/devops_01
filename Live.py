def load_game():
    
    print('Hello , Welcome to our Game Zone')
    
    counter = 1
    tries = 3
    while counter <= tries:
        
        choice = input("""
        Please choose a game to play:
        1. Memory Game        - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game         - guess a number and see if you chose like the computer
        3. Currency Roulette  - try and guess the value of a random amount of USD in ILS
        make a selection :     """)
        
        counter += 1
        
        if choice.isdigit() and (1 <= int(choice) <= 3):
            
            diff_counter = 1
            diff_tries = 3
            while diff_counter <= diff_tries:
                
                difficulty = input('Please choose game difficulty from 1 to 5 : ')
                
                diff_counter += 1
                          
                if difficulty.isdigit() and (1 <= int(difficulty) <= 5):
                                                         
                    print(f'You choose {difficulty} level , good luck...')
                    return

                else:
                    print("Not a valid number ! Try again...")
            
            return    
                
                    
load_game()


"""
this is the code , now you can import the functions from the file ans run them :
from <file name> import <function name>    -->    from Live import welcome, load_game 
notice:  that you have to be in the same folder directoty of the file  in the terminal, and then open from there the python shell ,and then  enter the "from import command ."

def load_game():
    
    print('Hello , Welcome to our Game Zone')
    
    counter = 1
    tries = 3
    while counter <= tries:
        
        choice = input("""
        Please choose a game to play:
        1. Memory Game        - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game         - guess a number and see if you chose like the computer
        3. Currency Roulette  - try and guess the value of a random amount of USD in ILS
        make a selection :     """)
        
        counter += 1
        
        if choice.isdigit() and (1 <= int(choice) <= 3):
            
            diff_counter = 1
            diff_tries = 3
            while diff_counter <= diff_tries:
                
                difficulty = input('Please choose game difficulty from 1 to 5 : ')
                
                diff_counter += 1
                          
                if difficulty.isdigit() and (1 <= int(difficulty) <= 5):
                                                         
                    print(f'You choose {difficulty} level , good luck...')
                    return

                else:
                    print("Not a valid number ! Try again...")
            
            return    
                
                    
load_game()
