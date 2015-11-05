#!/usr/bin/env python
from exercise3 import union, intersection, difference, MismatchedAttributesException

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Erin_Mib'


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

NON_IDENTICAL = [["Number", "First Name", "Surname", "Date of Birth"],
                 [9297, "Andy", "O'Malley", "12/12/58"],
                 [7432, "Barbara", "O'Malley", "03/05/76"],
                 [9824, "Carl", "Darkes", "07/04/77"]]


ADDITIONAL_ROWS = [["Number", "Surname", "Age"],
                   [7432, "O'Malley", 39],
                   [9824, "Darkes", 38],
                   [1346, "Shannan", 24],
                   [2954, "Ericson", 36],
                   [1425, "Tester", 82]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    result_extended = [["Number", "Surname", "Age"],
                       [7274, "Robinson", 37],
                       [7432, "O'Malley", 39],
                       [9824, "Darkes", 38],
                       [1346, "Shannan", 24],
                       [2954, "Ericson", 36],
                       [1425, "Tester", 82]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    # test for MismatchedAttributesException
    try:
        union(GRADUATES, NON_IDENTICAL)
    except MismatchedAttributesException:
        assert True

    # test for different row lengths
    assert is_equal(result_extended, union(GRADUATES, ADDITIONAL_ROWS))


def test_intersection():
    """
    Test intersection operation.
    """

    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    result_extended = [["Number", "Surname", "Age"],
                       [7432, "O'Malley", 39],
                       [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    # test for MismatchedAttributesException
    try:
        intersection(GRADUATES, NON_IDENTICAL)
    except MismatchedAttributesException:
        assert True

    # test for different row lengths
    assert is_equal(result_extended, intersection(GRADUATES, ADDITIONAL_ROWS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    result_extended = [["Number", "Surname", "Age"],
                       [1346, "Shannan", 24],
                       [2954, "Ericson", 36],
                       [1425, "Tester", 82]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

    # test for MismatchedAttributesException
    try:
        difference(GRADUATES, NON_IDENTICAL)
    except MismatchedAttributesException:
        assert True

    # test for different row lengths
    assert is_equal(result_extended, difference(ADDITIONAL_ROWS, GRADUATES))
