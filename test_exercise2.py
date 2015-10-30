#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    # test substring search
    assert find("Testing a string", "est", 0, 15) == 1

    # test with substring not found
    assert find("Testing a string again", "ask", 0, 20) == -1

    # test for a whitespace (single space) search in string
    assert find("Testing a string once more", " ", 0, 25) == 7

    # test for number as string in string with different characters
    assert find("abc 123 $!@", "2", 0, 10) == 5



def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

    # test substring multi search
    assert multi_find("Testing a string", "g", 0, 15) == "6,15"

    # test with substring not found
    assert multi_find("Testing a string again", "x", 0, 20) == ""

    # test for punctuation character as string in string with different characters
    assert multi_find("abc123$!@ abc123$!@ abc123$!@", "!", 0, 30) == "7,17,27"

    # test for a whitespace (single space) search in string
    # assert find("Testing a string once more", " ", 0, 25) == "7,9,16,21"