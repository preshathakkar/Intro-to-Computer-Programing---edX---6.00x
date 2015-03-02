import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    chars = string.ascii_uppercase
    d = {}
    i = 0

    for char in chars:
        d[char]=chars[(i + shift)%26]
        d[string.lower(char)]=string.lower(chars[(i + shift)%26])
        i+=1

    return d

import string

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    str1 = ''

    for char in text:
        if coder.get(char) == None:
            str1 += char
        else:
            str1 += coder.get(char)

    return str1

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """

    return applyCoder(text,buildCoder(shift))

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    for char in text:
        
