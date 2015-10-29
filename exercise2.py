#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Erin_Mib'


def find(input_string, substring, start, end):
    length_main = len(input_string)
    length_short = len(substring)
    t = ""
    index = 0
    for i in range(0, length_main):
        if input_string[i] == substring[0]:
            index = 0
            for j in range(0, length_short):
                if input_string[i + j] != substring[j]:
                    break
                else:
                    index += 1
                    if index == length_short:
                        return i
                        t = "NIL"
            break
    if t != "NIL":
        return -1

# find()


def multi_find(input_string, substring, start, end):
    length_main = len(input_string)
    length_short = len(substring)
    result = ""
    empty = ""
    index = 0
    alpha = []
    for i in range(0, length_main):
        if input_string[i] == substring[0]:
            index = 0
            for j in range(0, length_short):
                if input_string[i + j] != substring[j]:
                    break
                else:
                    index += 1
                    if index == length_short:
                        alpha.append(i)
                        result = "Got"
    if result != "Got":
        return empty
    else:
        return (str(alpha).strip("[]")).replace(" ", "")

# multi_find()