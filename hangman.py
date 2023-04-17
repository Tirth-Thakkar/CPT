import random
# This program makes use of the random module to randomly select a word form a list of words depending on the difficulty selected by the user 
# for more information here is the python documentation for the random module: https://docs.python.org/3/library/random.html and here is the 
# here is the documentation for the exact function used the choice function https://docs.python.org/3/library/random.html#functions-for-sequences
# link to the source code for the module https://github.com/python/cpython/blob/3.11/Lib/random.py


def hangman_display(remaining_guesses, sixth):
    # This function displays the hangman with the corresponding amount of body parts
    # determined by the remaining guesses and what is one sixth as determined by 
    # dividing the total guesses by 6 to get the number of guesses per body part (rounded using //).
    # Each section is displayed ranging till it reaches the next section.
    if remaining_guesses <= sixth * 6 and remaining_guesses > sixth * 5:
        print("  _______")
        print(" |/      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    
    elif remaining_guesses >= sixth * 6:
        print("  _______")
        print(" |/      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")

    elif remaining_guesses <= sixth * 5 and remaining_guesses > sixth * 4:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    
    elif remaining_guesses <= sixth * 4 and remaining_guesses > sixth * 3:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |       |")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|___")
    
    elif remaining_guesses <= sixth * 3 and remaining_guesses > sixth * 2:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|___")
    
    elif remaining_guesses <= sixth * 2 and remaining_guesses > sixth:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|/")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|___")
    
    elif remaining_guesses <= sixth and remaining_guesses > 0:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|/")
        print(" |       |")
        print(" |      /")
        print(" |")
        print("_|___")
    
    elif remaining_guesses <= 0:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|/")
        print(" |       |")
        print(" |      / \ ")
        print(" |")
        print("_|___")

def hangman(difficulty):
    # Defining the difficulty selection that the user can choose from corresponding to the game mode.
    difficulties = ["hard", "medium", "easy"]
    
    # Determines if the user made a valid selection for the difficulty if not the procedure will terminate and propmt the user to enter a valid difficulty.
    if difficulty.lower().strip() not in difficulties:
        print("Please enter a valid difficulty.")
        return
    # The following code is if the user selects a valid difficulty which depending on the choice will determine the word list that will be used to select words from 
    # along with number of incorrect guess the user is allowed to make.
    
    else:
        # Hard mode difficulty selection, words are longer, and the user is allowed 1 more incorrect guess more than the number of letters in the word. 
        if difficulty.lower().strip() == "hard":
            words = ["Programming", "Algorithms", "Cybersecurity", "Artificial Intelligence", "Cryptography", "Software engineering", "Parallel computing", "Computational thinking", "Machine learning", "Information retrieval", "Microarchitecture", "Object oriented programming", "Computer networking", "Distributed systems", "Cloud computing", "Human-computer interaction", "Data structures", "Operating systems", "Virtualization", "Multi threading"]
            
            # Use of the choice function from the random module link: https://docs.python.org/3/library/random.html#functions-for-sequences
            chosen_word = random.choice(words).lower().replace(" ", "").strip()
            max_guess = len(chosen_word) + 1
            print("Mode: Hard")

        elif difficulty.lower().strip() == "medium":
            # Medium mode difficulty selection, words are shorter than hard but slightly longer than easy, and the user is allowed 10 more incorrect guesses more than the number of letters in the word.
            words = ["Buffer", "Cache", "Kernel", "Packet", "Python", "Script", "Socket", "Thread", "Cookie", "Object", "Router", "Server", "Vector", "Boolean", "Element", "Firefox", "Cluster", "Encoder", "Firewall", "Latency"]
            
            # Use of the choice function from the random module link: https://docs.python.org/3/library/random.html#functions-for-sequences
            chosen_word = random.choice(words).lower().replace(" ", "").strip()
            max_guess = len(chosen_word) + 10
            print("Mode: Medium")

        elif difficulty.lower().strip() == "easy":
            # Easy mode difficulty selection, words are short no longer than 4 letters, and the user is allowed 15 more incorrect guesses more than the number of letters in the word.
            words = ["Byte", "Code", "Loop", "HTML", "CSS", "Java", "Lisp","Ruby", "Perl", "PHP", "Unix", "SQL", "XML", "YAML", "FPGA", "CPU", "GPU", "IDE", "RAID", "Enum"]
            
            # Use of the choice function from the random module link: https://docs.python.org/3/library/random.html#functions-for-sequences
            chosen_word = random.choice(words).lower().replace(" ", "").strip()
            max_guess = len(chosen_word) + 15
            print("Mode: Easy")
    
    # Setting up the hangman display function and initial display when the hangman game starts. 
    total_guesses = max_guess
    sixth = total_guesses // 6    
    # Letter display is a list that will be replaced with correct letters as the game goes no corresponding to the position of the letter in the word
    letter_display = ['_'] * len(chosen_word)
    hangman_display(6,1)
    print(' '.join(letter_display))

    # Beginning of the game loop that will terminate when the user runs out of incorrect guesses or guesses the word correctly.
    while max_guess > 0:
        warning = 0
        # An input is taken from the user to guess a letter or request a whole word guess option.
        letter_guess = input("Guess a letter (input 'wordguess' to guess the whole word): ").lower().strip()
        
        # If the user inputs the wordguess option the user will be prompted to enter a word guess as input and the game will check if the word is correct or not.
        # If not correct the user will have one deducted from their remaining incorrect guess allotted to them the code for that is another segment.
        
        if letter_guess == "wordguess":
            word_guess = input("Guess the word: ").strip().lower()
            if word_guess == chosen_word:
                hangman_display(max_guess, sixth)
                for char in chosen_word:
                    print(char, end=' ')
                print(f"\nCorrect! Your word matched the word {chosen_word}.")
                break

        
        # If the user inputs more than a single letter and not the specified terms wordguess or stop the user will be prompted to enter a single letter.
        # They will not have a guess deducted from their remaining incorrect guesses.
        elif len(letter_guess) != 1 and letter_guess != "wordguess" and letter_guess != "stop":
            print("Please enter a single letter.")
            warning += 1
        
        # If the a single letter is inputted and is within the selected word which was randomly chosen earlier using the choice function from the random module
        # from the list of words corresponding to the difficulty the user selected the letter will be displayed in the letter display list in the position
        # that it is in the word. The user will be indicated that they have guessed correctly and will be shown the current state of the word.
        
        elif letter_guess in chosen_word:
            # A for loop that iterates for the range of the length of the word and till it reaches the index of the letter that the user guessed.
            # Using the index represented by the variable char the index of the list letter_display will be replaced with the letter that the user guessed.
            # which will be displayed to the user along with the hangman display and the current state of the word along with the number of incorrect guesses
            # the user has left, the use will not be deducted from their remaining incorrect guesses.
            
            for char in range(len(chosen_word)):
                if chosen_word[char] == letter_guess:
                    letter_display[char] = letter_guess
            hangman_display(max_guess, sixth)
            print(' '.join(letter_display))
            print(f"Correct! you have {max_guess} incorrect guesses left.")
        
        # Allowing the use to stop the game at any time by inputting in the term stop.
        # The game will terminate and the user will be shown the word that they were trying to guess.
        if letter_guess == "stop":
            print(f"game stopped by user request. The word was {chosen_word}.")
            break

        # When letter display has completely been replaced by the characters that was in the word that was randomly chosen earlier using the choice function from the random module
        # the program will terminate and the user will be shown the word that they were trying to guess and will be indicated that they have won the game and will be shown the word.
        # This is done by using the join function to join the list letter_display into a string and then comparing it to the chosen word. 
        if chosen_word == ''.join(letter_display):
            hangman_display(max_guess, sixth)
            print(' '.join(letter_display))
            print(f"You win! The word was {chosen_word}.")
            break

        # If the user inputs a letter that is not in the word that was randomly chosen earlier using the choice function from the random module and the has not run out of incorrect guesses
        # the user will be shown the hangman display and the current state of the word along with the number of incorrect guesses the user has left, and one will be deducted from the remaining 
        # incorrect guesses the user has left. If the user has guessed the word incorrectly they are also deducted here.

        elif letter_guess not in chosen_word and warning == 0:
            max_guess -= 1
            hangman_display(max_guess, sixth)
            print(' '.join(letter_display))
            print(f"Incorrect. You have {max_guess} incorrect guesses left.")
            
    # If the while loop terminates the else condition will execute and the user will be shown the hangman display and the word that they were trying to guess and will be indicated that they have lost the game.
    else:
        hangman_display(max_guess, sixth)
        for char in chosen_word:
            print(char, end=' ')
        print(f"\nGame over! The word was {chosen_word}. YOU LOSE!")
        

# PROCEDURE [CALLS

# Call 1:
print("-----------------Call 1-----------------\n")
hangman("easy")

# Call 2:
print("\n-----------------Call 2-----------------\n")
hangman("medium")
