#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    numcols_table1 = len(table1[0])
    numcols_table2 = len(table2[0])
    indices1 = range(len(table1))
    indices2 = range(len(table2))
    indices = [indices1, indices2]
    indices = sum(indices, [])

    if numcols_table1 != numcols_table2:
        return MismatchedAttributesException
    else:
        for i in range(0, numcols_table2):
            if table1[0][i] != table2[0][i]:
                return MismatchedAttributesException
            else:
                continue
        new_table = [table1, table2]
        new_table = sum(new_table, [])
        zipped = zip(indices, new_table)
        zipped.sort()
        new_table_sorted = [x for y, x in zipped]
        new_table_out = remove_duplicates(new_table_sorted)
        return new_table_out


def intersection(table1, table2):

    numcols_table1 = len(table1[0])
    numcols_table2 = len(table2[0])
    if numcols_table1 != numcols_table2:
        return MismatchedAttributesException
    else:
        for i in range(0, numcols_table2):
            if table1[0][i] != table2[0][i]:
                return MismatchedAttributesException
            else:
                continue
        new_table = []
        for row in table1:
            if row in table2:
                new_table.append(row)
        return new_table


def difference(table1, table2):

    numcols_table1 = len(table1[0])
    numcols_table2 = len(table2[0])
    if numcols_table1 != numcols_table2:
        return MismatchedAttributesException
    else:
        for i in range(0, numcols_table2):
            if table1[0][i] != table2[0][i]:
                return MismatchedAttributesException
            else:
                continue
        new_table = [table1[0]]
        for row in table1:
            if row not in table2:
                new_table.append(row)
        return new_table


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


# union()
# intersection()
# difference()
