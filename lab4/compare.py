#!/usr/bin/env python

# File:             compare.py
# Author:           Brad Anderson
# Date:             February 9, 2018
# Project:          ME499 Lab 4
# Description:      Compares word contents of two text files
# Collaborators:    None
# Sources Used:
#   -- Uniqify Lists (No Longer Used) --
#   https://www.peterbe.com/plog/uniqifiers-benchmark

import sys
import string


def checkArgumentCount():
    filetype = '.txt'
    if not len(sys.argv) == 3:
        sys.exit('Please enter two arguments')
    if (not sys.argv[1].endswith(filetype)
        or not sys.argv[2].endswith(filetype)):
            sys.exit('Please enter ".txt" files')
# end def


def printWordCount(a_arg1,s_arg1, a_arg2,s_arg2):
    print sys.argv[1] + ':'
    print "  " + str(len(a_arg1)) + ' words'
    print "  uniqie: " + str(len(s_arg1))
    print sys.argv[2] + ':'
    print "  " + str(len(a_arg2)) + ' words'
    print "  unique: " + str(len(s_arg2))
#end def


def readFilesToSortedLists(file1, file2):

    lines = [None, None]
    
    for i, file in enumerate([file1, file2]):
        with open(file) as f:
            text = f.readlines()
            lines[i] = [word.strip().translate(None,
                        string.punctuation)
                    for line in text
                    for word in line.lower().strip().split()]

    return sorted(lines[0]), sorted(lines[1])
# end for


def countSimilarWords(s1, s2):
    similar = []
    for word in s1:
        if word in s2:
            similar.append(word)
    return set(similar)
# end def


def printCommonWords(s_text, s_dict, s_common):
    print 'Only', sys.argv[1], ': ', len(s_text) - len(s_common)
    print 'Only', sys.argv[2], ': ', len(s_dict) - len(s_common)
    print 'Both files: ', len(s_common)
# MAIN
if __name__ == "__main__":

    checkArgumentCount()
    a_text, a_dict = readFilesToSortedLists(sys.argv[1], sys.argv[2])
    s_text, s_dict = (set(a_text), set(a_dict))
    printWordCount(a_text,s_text, a_dict,s_dict)
    s_common = countSimilarWords(s_text, s_dict)
    printCommonWords(s_text, s_dict, s_common)

    
# end main


