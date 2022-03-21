# Hangman game

import random
from re import U

WORDLIST_FILENAME = "./words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded. \n-----------------------------------\n")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    return all([False if i not in lettersGuessed else True for i in secretWord])


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    return ''.join(i + " " if i in lettersGuessed else "_ " for i in secretWord).strip()


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    return ''.join(i for i in "abcdefghijklmnopqrstuvwxyz" if i not in lettersGuessed)


def hangman(secretWord):
    secretWord = secretWord.lower()
    print("\n-----------------------------------\nI am thinking of a word that is " +
          str(len(secretWord)) + " letters long. \n-------------")

    lettersGuessed = set()
    guessed = getGuessedWord(secretWord, lettersGuessed)
    guess_left = 8
    while guess_left > 0:
        available = getAvailableLetters(lettersGuessed)
        print("You have " + str(guess_left) +
              " guesses left. \nAvailable letters: " + available)
        guess = input("Please guess a letter: ").lower()

        currentGuess = ""

        if len(guess) > 1:
            print(f"Only one letter is allowed as the guess!")
        elif guess.isnumeric():
            print(f"Only letters are allowed as the guess!")
        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + currentGuess)
        elif guess in secretWord:
            lettersGuessed.add(guess)
            currentGuess = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: " + currentGuess)
        elif guess not in secretWord:
            lettersGuessed.add(guess)
            currentGuess = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! That letter is not in my word: " + currentGuess)
            guess_left = guess_left - 1

        guessed = currentGuess
        print("-------------")

        end = isWordGuessed(secretWord, lettersGuessed)
        if end:
            print("Congratulations, you won!")
            print("\n-----------------------------------")

            break

    if guess_left == 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        print("\n-----------------------------------")


def user_defined():
    return input("Enter the Word you chose: ")

if __name__ == '__main__':
    while 0 < 1:
        print('''Welcome to the game Hangman! \n1. Play a Normal Game of Guessing! \n2. Ask a friend to guess a word defined by You!\n0. Exit
        ''')
        choice = int(input("Enter your Choice!: "))

        if choice == 1:
            secretWord = chooseWord(wordlist).lower()
            hangman(secretWord)

        elif choice == 2:
            secretWord = input("Enter the Word you chose: ")
            if secretWord.isalpha():
                hangman(secretWord)
            elif secretWord.isalnum():
                user_defined()

        elif choice == 0:
            exit()
        else:
            print("Invalid Choice!")
            continue
