#!/usr/bin/env python3

"""
Helper functions
"""

def remove_illegal_chars(filename):

    """ Removes illegal characters from string """

    keepcharacters = (' ','_')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()
