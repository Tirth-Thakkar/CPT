import random

# The random python module is used in this program to randomly select a word based on a users topic selection. 
# To gain further information about the random module that is used in this program please visit the documentation at https://docs.python.org/3/library/random.html
# Specifically the choice function is used in this program to randomly select a word from a list of words to learn about this specifically here is the link to that 
# portion of the docs: https://docs.python.org/3/library/random.html#functions-for-sequences
# To see the source code for the random python module please visit: https://github.com/python/cpython/blob/3.11/Lib/random.py

def wordle(topic):
    
    # Declaring the possible topic selection and creating the Wordle board that will be used to display the users guesses and their correctness.
    topics = ['computer', 'foods', 'flowers']
    wordle_board = [['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_']]
    
    
    if topic.lower().strip() in topics:
        if topic.lower().strip() == "computer":
            
            # Computer topic selection if the user selected the topic as computer only words that are computer related can be selected as the answer.
            PossibleWords = ['mouse', 'nodes', 'mysql', 'swift', 'scala', 'julia', 'emacs', 'xcode', 'gnome', 'unity', 'linux', 'macos', 'opera', 'brave', 'links', 'apple']
            
            # Choice Function from the random module is used below: https://docs.python.org/3/library/random.html#functions-for-sequences
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Computer')
    
        elif topic.lower().strip() == 'foods':
            
            # Food topic selection if the selected user topic is foods only words that are food related can be selected as the answer.
            PossibleWords = ['gouda', 'swiss', 'cream', 'bagel', 'dough', 'colby', 'comte', 'kefir', 'bread', 'pizza', 'onion', 'salad', 'sushi', 'soups', 'sugar', 'pasta']
            
            # Choice function from the random module is used below: https://docs.python.org/3/library/random.html#functions-for-sequences
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Foods')
        
        
        elif topic.lower().strip() == 'flowers': 
            
            # Flower topic if the user chooses flowers as their topic only a flower word may be selected as the answer. 
            PossibleWords = ['roses', 'daisy', 'tulip', 'lilac', 'lilly', 'peony', 'poppy', 'lotus', 'aster', 'canna', 'holly', 'pansy', 'petal', 'bloom', 'viola', 'oxlip']
            
            # Choice function from the random module is used below: https://docs.python.org/3/library/random.html#functions-for-sequences
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Flowers')
    else: 
        # Prevents user from inputting an invalid term into the function and not getting a word
        print('You have chosen an invalid topic the only available topics are:', end=' ')
        print(*topics, sep=', ')
        return
    
    # Initializing the runs variable to be able to index the grid
    runs = 0
    print("Welcome to \033[1mnot\033[0m Worldle!")
    
    # While loop that contains the game code will run till the user has reached their 5th guess
    # <= to prevent the user from getting an index error 
    while runs <= 4:
        # Flagged variable is present to prevent user from losing a guess if they enter an invalid input
        flagged = False
        
        # For every turn the loop will print the entire board with the user's prior guesses and their respective correctness
        for board in wordle_board:
            print(*board)
        
        # Use input to allow the user to able to input a new word per turn
        user_guess = input('\nGuess a 5 letter word. Enter stop to end the game: ').strip().lower()
        
        # If the input is valid by being 5 letters long and not terminating the game with stop 
        # The program will begin checking the user's input for correctness
        if len(user_guess) == 5 and user_guess != 'stop' and user_guess in PossibleWords:
            
            # For loop that will iterate through the range represented by the length of the user's guess
            for temporary_letter_index in range(len(user_guess)):
                # Corresponding to the turn the board from the list of boards will be indexed and each letter of the user's 
                # guess will be placed corresponding to the index of the letter into the board
                wordle_board[runs][temporary_letter_index] = user_guess[temporary_letter_index]
            
            # If the user's guess matches the selected word determined earlier by the choice function from the random module 
            # the user will wind and game will terminate
            if user_guess == selected_word:
                
                # Displays the board with the correct answer shown in bold corresponding to the user's correct guess
                # in the same style as the rest of the program
                for winning_letter in range(len(user_guess)):
                    wordle_board[runs][winning_letter] = '\033[1m' + user_guess[winning_letter] + '\033[0m'
                
                # Print the completed board and then a winning message
                for board in wordle_board:
                    print(*board)
                print('You have guessed the word correctly!')
                break
            
            # If the user's guess does not perfectly match the selected word the program will perform additional checks
            elif user_guess != selected_word and user_guess in PossibleWords:
                
                # For every corresponding index in the range created by the length of the user's guess
                for letter_index in range(len(user_guess)):
                    
                    # If a letter in the user's guess is in the selected and the position is correct as well then the letter 
                    # will be displayed in bold on the board by replacing the corresponding index with the letter in bold
                    if user_guess[letter_index] in selected_word and user_guess[letter_index] == selected_word[letter_index]:
                        wordle_board[runs][letter_index] = '\033[1m' + user_guess[letter_index] + '\033[0m' 

                    # If a letter in the letter's guess is present in one or more places within the selected word but not 
                    # in the correct position then the letter will be displayed in italics on the board by replacing the
                    # corresponding index with the letter in italics
                    elif user_guess[letter_index] in selected_word and user_guess[letter_index] != selected_word[letter_index]:
                        wordle_board[runs][letter_index] = '\033[3m' + user_guess[letter_index] + '\033[0m'

        # if the user's input is stop then the game will terminate with a corresponding message
        elif user_guess == 'stop':
            print(f'You have stopped the game. The correct word was {selected_word}')
            break
        
        # If the user's input not 5 letters long then the program will set the flagged boolean value to true 
        # preventing the user from losing a turn and the runs variable from being incremented 
        else:
            print('You have not entered a 5 letter word. Or not in the word bank for your topic.')
            flagged = True
        
        # If the run is flagged the if block will prevent the runs from being incremented and the user from being penalized
        if not flagged: 
            runs += 1
    
    # If the user has reached their 5th turn and has not guessed the word the program will display the board with the correct word
    # and a message informing the user that they have lost the game
    if runs == 5:
        for board in wordle_board:
            print(*board)
        print(f'You lost the game the correct word was {selected_word}')

# Function Calls
print('--------------Call 1--------------\n')
wordle('foods')

print('\n--------------Call 2--------------\n')
wordle('flowers')