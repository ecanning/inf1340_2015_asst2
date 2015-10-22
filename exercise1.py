#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
#    result = ""


    pig_latin = "ay"

    word = str(word)

    if len(word) > 0 and word.isalpha():
        word = word.lower()
        first_letter = word[0] # find first vowel
        piglatin_word = word + first_letter + pig_latin
        piglatin_word = word[1:len(word)] + first_letter + pig_latin
        print piglatin_word

    elif ValueError:
        return ValueError

    return piglatin_word

# pig_latinify(word)

#    return result