#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Erin_mib'


def pig_latinify(word):
    """
    This function takes an argument of a single word and turns it into Pig Latin

    :param: input string in single word
    :return: output string in single word in "pig latin": if first letter is a vowel,
    return word with "yay" appended to the end, otherwise consonants before first vowel
    appended to end of word, followed by "ay"
    :raises: Value Error raised if input is empty, or not a word

    """

    a = 0
    vowels = ("a", "e", "i", "o", "u","A","E","I","O","U")
    if len(word) > 0 and word.isalpha():
        for index in word:
            first_letter = word[a]
            if first_letter in vowels:
                return word + "yay"
            else:
                a += 1
                letter = word[a]
                if letter in vowels:
                    return word[a:] + word[:a] + "ay"
    elif ValueError:
        return ValueError
    elif TypeError:
        return TypeError

# pig_latinify()