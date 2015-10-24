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

    words = word.split()
    test_word = ""

    if len(word) > 0 and word.isalpha():
        for test_word in words:
            if test_word[0] in "aeiou":
                print test_word + "yay"
            else:
                for i in range(len(word)):
                    sum = 0
                    while sum == 0:
                        if word[i] in "aeiou":
                            print word[i:] + word[:i] + "ay"
                            sum += 1
                        else:
                            sum += 1

    elif ValueError:
        return ValueError

#pig_latinify()