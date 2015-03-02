# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for char1 in secretWord:
        for char2 in lettersGuessed:
            if char1 == char2:
                 count += 1

    if count >= len(secretWord):
        return True
    else:
        return False
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = '_' * len(secretWord)
    for char1 in secretWord:
        for char2 in lettersGuessed:
        
            if char1 == char2:
                c = secretWord.count(char1)
                if c == 1:
                    s = s[:secretWord.index(char1)] + char1 +s[secretWord.index(char1)+1:]
                elif c == 2:
                    s = s[:secretWord.index(char1)] + char1 +s[secretWord.index(char1)+1:]
                    s = s[:secretWord.index(char1,secretWord.index(char1)+1)] + char1 +s[secretWord.index(char1,secretWord.index(char1)+1)+1:]
                elif c == 3:
                    i = secretWord.index(char1)
                    s = s[:i] + char1 +s[i+1:]
                    s = s[:secretWord.index(char1,i+1)] + char1 +s[secretWord.index(char1,i+1)+1:]
                    j = secretWord.index(char1,i+1)
                    s = s[:secretWord.index(char1,j+1)] + char1 +s[secretWord.index(char1,j+1)+1:]
                    
    if len(secretWord) == len(s):
        return s
    else:
        return s[:len(secretWord)]


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = string.ascii_lowercase
    s1 = string.ascii_lowercase
    for char in s:
        if char in lettersGuessed:
            s1 = s1[:s1.index(char)]+s1[s1.index(char)+1:]

    return s1
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    i = 1
    lettersGuessed = []
    mistakesMade = 0
    availableLetters = string.ascii_lowercase
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    while mistakesMade < 8:
        print '-----------'
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            break
        print 'You have ' + str(8-mistakesMade) + ' guesses left'
        print 'Available Letters: ' + availableLetters
        s = raw_input('Please guess a letter: ')
        lettersGuessed.append(s)
        if s in availableLetters:
            if s in secretWord:
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
                availableLetters = getAvailableLetters(lettersGuessed)
            else:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                availableLetters = getAvailableLetters(lettersGuessed)
                mistakesMade +=1
        else:
            print 'Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed)
            
    if(mistakesMade >= 8):
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
