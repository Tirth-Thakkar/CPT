import random

def wordle(topic):
    
    topics = ['computer', 'cheese', 'colors']
    wordle_board = [['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_'], ['_','_','_','_','_']]
    
    if topic.lower().strip() in topics:
        
        if topic.lower().strip() == "computer":
            PossibleWords = ['mouse', 'nodes', 'mysql', 'swift', 'scala', 'julia', 'emacs', 'xcode', 'gnome', 'unity', 'linux', 'macos', 'opera', 'brave', 'links', 'apple']
            selected_word = random.choice(PossibleWords)
            print('You have chosen the topic: Computer')
        
        elif topic.lower().strip() == 'foods':
            PossibleWords = ['gouda', 'swiss', 'cream', 'bagel', 'dough', 'colby', 'comte', 'kefir', 'bread', 'pizza', 'onion', 'salad', 'sushi', 'soup', 'sugar', 'pasta']
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
    for board in wordle_board:
        runs += 1
        print(*board)
        user_guess = input('Guess a 5 letter word.')

        if len(user_guess) == 5:
            user_guess = wordle_board
            if user_guess == selected_word:
                print('You have guessed the word correctly!')
                break
            elif user_guess != selected_word:
                pass 
        else:
            print('You have not entered a 5 letter word.')
            break

wordle('cheese')