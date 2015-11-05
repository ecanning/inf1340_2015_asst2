#!/usr/bin/env python
from exercise1 import pig_latinify
""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Erin_Mib'


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    # test with multiple vowels in word
    assert pig_latinify("wonderful") == "onderfulway"

    # test with  vowels in uppercase in word
    assert pig_latinify("Apple") == "Appleyay"

    # test with non-letters in string
    try:
        pig_latinify("2d")
    except ValueError:
        assert True

    # test with integer instead of string
    try:
        pig_latinify(34)
    except TypeError:
        assert True

    # test with empty string
    try:
        pig_latinify("")
    except ValueError:
        assert True
