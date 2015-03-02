from ps4a import *
import time
import string


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    max_score = 0

    best_word = None

    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, HAND_SIZE)
            if score > max_score:
                max_score = score
                best_word = word

    return best_word
    


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    total_score = 0
    game_done = False
    
    while game_done == False:

        if calculateHandlen(hand) == 0:
            game_done == True
            break;

        
        else:
            print "Current Hand: "
            displayHand(hand)
            word = compChooseWord(hand, wordList)
            if word == None:
                print 'Total score: '+str(total_score)+' points.'
                break;
            else:
                total_score += getWordScore(word, HAND_SIZE)
                hand = updateHand(hand, word)
                print '"'+word+'" earned '+str(getWordScore(word, HAND_SIZE))+' points. Total: '+str(total_score)+' points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    game_on = True
    hand = {}

    while game_on == True:
        print
        c = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        if c == 'e':
            game_on = False
            break;

        elif c == 'r':
            if hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                player = raw_input('Enter u to play, or c to ask computer to play: ')
                hand2 = hand.copy()
                if player == 'u':
                    playHand(hand2, wordList, HAND_SIZE)
                elif player == 'c':
                    compPlayHand(hand2, wordList)
                else:
                    print 'Invalid command'
                
        elif c == 'n':
            hand = dealHand(HAND_SIZE)
            hand2 = hand.copy()
            player = raw_input('Enter u to play, or c to ask computer to play: ')
            if player == 'u':
                playHand(hand2, wordList, HAND_SIZE)
            elif player == 'c':
                compPlayHand(hand2, wordList)
            else:
                print 'Invalid command'

        else:
            print 'Invalid command.'
    
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


