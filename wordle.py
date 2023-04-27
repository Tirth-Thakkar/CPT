import random

# The random python module is used in this program to randomly select a word based on a users topic selection. 
# To gain further information about the random module that is used in this program please visit the documentation at https://docs.python.org/3/library/random.html
# Specifically the choice function is used in this program to randomly select a word from a list of words to learn about this specifically here is the link to that portion of the docs: https://docs.python.org/3/library/random.html#functions-for-sequences
# To see the source code for the random python module please visit:    

def wordle(topic):
    
    # Declaring the possible topic selection and creating the Wordle board that will be used to display the users guesses and their correctness.
    topics = ['computer', 'foods', 'colors']
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
            PossibleWords = ['roses', 'daisy', 'tulip', 'lilac', 'lilly', 'peony', 'orchid', 'poppy', 'lotus', 'aster', 'canna', 'holly', 'pansy', 'petal', 'bloom', 'viola']
            
            # Choice function from the random module is used below: https://docs.python.org/3/library/random.html#functions-for-sequences
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Flowers')
    else: 
        print('You have chosen an invalid topic the only available topics are:', end=' ')
        print(*topics, sep=', ')
        return
    
    runs = 0
    print("Welcome to \033[1mnot\033[0m Worldle!")
    while runs <= 4:
        flagged = False
        marked_indices = []
        for board in wordle_board:
            print(*board)
        user_guess = input('\nGuess a 5 letter word. Enter stop to end the game: ').strip().lower()

        if len(user_guess) == 5 and user_guess != 'stop':
            for temporary_letter_index in range(len(user_guess)):
                wordle_board[runs][temporary_letter_index] = user_guess[temporary_letter_index]
            if user_guess == selected_word:
                for winning_letter in range(len(user_guess)):
                    wordle_board[runs][winning_letter] = '\033[1m' + user_guess[winning_letter] + '\033[0m'
                for board in wordle_board:
                    print(*board)
                print('You have guessed the word correctly!')
                break
            elif user_guess != selected_word:
                for letter_index in range(len(user_guess)):
                    if user_guess[letter_index] in selected_word and user_guess[letter_index] == selected_word[letter_index]:
                        wordle_board[runs][letter_index] = '\033[1m' + user_guess[letter_index] + '\033[0m' 
                        marked_indices.append(letter_index)

                    elif user_guess[letter_index] in selected_word and user_guess[letter_index] != selected_word[letter_index] and letter_index not in marked_indices:
                        wordle_board[runs][letter_index] = '\033[3m' + user_guess[letter_index] + '\033[0m'
                        marked_indices.append(letter_index)
        
        elif user_guess == 'stop':
            print(f'You have stopped the game. The correct word was {selected_word}')
            break
        
        else:
            print('You have not entered a 5 letter word.')
            flagged = True
        if not flagged: 
            runs += 1

    if runs == 5:
        for board in wordle_board:
            print(*board)
        print(f'You lost the game the correct word was {selected_word}')

wordle('foods')

