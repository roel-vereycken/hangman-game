import random
import string

alphabet = set(string.ascii_uppercase)  # Letters in the alphabet


# This is a function that returns a random element(= word) from a list in uppercase
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:  # Makes shure that we don't return a word that contains a "-" or a space
        word = random.choise(words)

    return word.upper()


# This is a function that validates that the user has entered a valid symbol
def get_correct_user_input(user_input):
    while len(user_input) > 1 or user_input.upper() not in alphabet:
        user_input = input("You typed an invalid value: " +
                           user_input + ". Please try again.")
    return user_input.upper()
