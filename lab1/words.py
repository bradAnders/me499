#!/usr/bin/env python

# Author:           Brad Anderson
# Date:             January 16, 2018
# File:             ME499 Lab0 letter count
# Description:      Counts the number of time a letter appears in a word
# Collaborators:    Kenzie Brian

def letter_count(string1, string2):

    if not len(string2) == 1:
        return None
    # end if

    return string1.lower().count(string2.lower(), 0, len(string1.lower()))

# end letter_count
if __name__ == '__main__':

    print letter_count('halLway', 'L')
