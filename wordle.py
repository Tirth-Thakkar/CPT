import random

def wordle(topic):
    
    topics = ['computer', 'foods', 'colors']
    wordle_board = [['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_']]
    
    if topic.lower().strip() in topics:
        
        if topic.lower().strip() == "computer":
            PossibleWords = ['mouse', 'nodes', 'mysql', 'swift', 'scala', 'julia', 'emacs', 'xcode', 'gnome', 'unity', 'linux', 'macos', 'opera', 'brave', 'links', 'apple']
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Computer')
        
        elif topic.lower().strip() == 'foods':
            PossibleWords = ['gouda', 'swiss', 'cream', 'bagel', 'dough', 'colby', 'comte', 'kefir', 'bread', 'pizza', 'onion', 'salad', 'sushi', 'soups', 'sugar', 'pasta']
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Foods')
        
        elif topic.lower().strip() == 'flowers': 
            PossibleWords = ['roses', 'daisy', 'tulip', 'lilac', 'lilly', 'peony', 'orchid', 'poppy', 'lotus', 'aster', 'canna', 'holly', 'pansy', 'petal', 'bloom', 'viola']
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Flowers')
    else: 
        print('You have chosen an invalid topic the only available topics are:', end=' ')
        print(*topics, sep=', ')
        return
    
    runs = 0
    flagged = False
    print("Welcome to \033[1mnot\033[0m Worldle!")
    while runs <= 4:
        for board in wordle_board:
            print(*board)
        user_guess = input('Guess a 5 letter word. Enter stop to end the game').strip().lower()

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
                    elif user_guess[letter_index] in selected_word and user_guess[letter_index] != selected_word[letter_index]:
                        wordle_board[runs][letter_index] = '\033[3m' + user_guess[letter_index] + '\033[0m'
        
        elif user_guess == 'stop':
            print(f'You have stopped the game. The correct word was {selected_word}')
            break
        
        else:
            print('You have not entered a 5 letter word.')
            flagged = True
        if not flagged: 
            runs += 1

    if runs == 5:
        print(f'You lost the game the correct word was {selected_word}')
wordle('foods')

