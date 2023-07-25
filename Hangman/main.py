from random import randint
import requests
import json

BASE_URL = "https://random-word-api.herokuapp.com/word?length="

def get_name() -> str:
    """Asks user for their username and returns it"""
    have_name = False
    while have_name is False:
        username = input("Enter username:")
        print("Username is: " + username)
        have_answer = False
        while have_answer is False:
            answer = input("Is this correct? (y/n)")
            if answer == "y":
                return username
            elif answer == "n":
                have_answer = True


def get_difficulty() -> str:
    """Asks user for their choice of difficulty level and returns it"""
    have_level = False
    while have_level is False:
        print("Please choose a difficulty level. \n1. Easy (3-5 letters)\n2. Medium (6-8 letters)\n3. Hard (9-12 letters)")
        level = input("What difficulty level would you like? (1/2/3)")
        if level == "1":
            print("You have chosen: Easy")
            return "Easy"
        elif level == "2":
            print("You have chosen: Medium")
            return "Medium"
        elif level == "3":
            print("You have chosen: Hard")
            return "Hard"
        


def get_word(difficulty: str) -> str:
    """Takes in a difficulty level and returns a word based on that level"""
    if difficulty == "Easy":
        word_length = randint(3, 5)
    elif difficulty == "Medium":
        word_length = randint(6, 8)
    else:
        word_length = randint(9, 12)
    
    response = requests.get(f"{BASE_URL}{word_length}", timeout=5)
    return(response.json()[0].upper())


def find_letter_indexes(letter, word) -> list:
    """Takes in a letter and a word and finds the indexes of each occurrence of that letter in the word"""
    return [i for i, ltr in enumerate(word) if ltr == letter]


def game(word):
    """Plays game of Hangman"""
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print("Let's play!")
    lives = 10
    word = list(word.upper())
    shown_word = []
    for letter in word:
        shown_word.append("_")
    letters_used = []
    print(f"You have {lives} lives left")
    while lives > 0:
        has_letter = False
        while has_letter is False:
            print(" ".join(shown_word))
            letter = input("Choose a letter").upper()
            if letter in letters_used:
                print(f"You have already used {letter}. Please choose again.")
            elif letter in letters:
                print(f"You have chosen: {letter.upper()}")
                letters_used.append(letter)
                has_letter = True
            else:
                print("That is not a letter.")
    
        letter_indexes = find_letter_indexes(letter.upper(), word)

        if len(letter_indexes) == 0:
            print(f"The word does not contain a {letter}. You lose a life!")
            lives -= 1
            if lives > 1:
                print(f"{lives} lives remaining.")
            elif lives == 0:
                print("0 lives remaining. You lose!")
                return None
            else:
                print("You only have one life remaining!")
        else:
            print("Correct!")
            for index in letter_indexes:
                shown_word[index] = letter
            print(" ".join(shown_word))
            if '_' not in shown_word:
                print("Congratulations! You win!")
                return None


def want_to_play_again() -> bool:
    """Asks user if they want to play again, if yes, restarts game"""
    have_answer = False
    while have_answer is False:
        answer = input("Do you want to play again? (y/n) ").upper()
        if answer == "Y":
            print("Great! Let's play again!")
            return True
        elif answer == "N":
            print("Okay, bye for now!")
            return False

if __name__ == "__main__":
    username = get_name()
    difficulty = get_difficulty()
    word = get_word(difficulty)
    play_game = True
    while play_game is True:
        word = get_word(difficulty)
        game(word)
        play_game = want_to_play_again()

