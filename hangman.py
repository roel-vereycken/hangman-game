from helpers import *
from words import words


def hangman():
    word = get_valid_word(words)  # A random word
    word_letters = set(word)  # Letters in the word
    used_letters = set()  # Guessed letters

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        # Letters used
        print("You have " + str(lives) + " lives left.")
        print("You have already used these letters: ", ", ".join(
            used_letters))  # " ".join(["a", "b", "c"]) => "a, b, c"

        # Show current word
        word_list = [
            letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        print("")  # Empty rule in console

        # Get user input
        user_input = input("Guess a letter: ").upper()
        user_input = get_correct_user_input(
            user_input)  # Loops until the input is valid
        print("")  # Empty rule in console

        # Game logic
        used_letter = user_input
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)
            else:
                lives = lives - 1  # Takes a live away
                print("The letter is not in the word.")

        elif used_letter in used_letters:
            print("You already used this letter: " +
                  used_letter + ". Please try another one.")
            print("")

    # Gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died. The word was " + word + ".")
    else:
        print("You guessed the word " + word + "!!!")
