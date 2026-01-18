import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    middle_number = len(poss_values) // 2  
    return poss_values[middle_number]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val:
        HigherOrLower = "h"
    else:
        HigherOrLower = "l"
    
    if HigherOrLower == user_input:
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    LetterFound = False
    WordList = list(word)
    for character_index in range(len(WordList)):
        if WordList[character_index] == letter:
            LetterFound = True
            board[character_index] = letter
    
    if LetterFound == True:
        print("Well done! " + letter + " is in the word")
        return True
    else:
        print("Sorry, " + letter + " is not in the word")
        return False

