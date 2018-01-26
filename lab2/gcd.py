#!usr/bin/env python

# File:             gcd.py
# Title:            ME499 Lab2 - Greatest common denominator
# Author:           Brad Anderson
# Date:             January 32, 2018
# Description:      Exercise 6.8 
# Collaborators:    Kenzie Brian


# Returns the greatest common divisor of two numbers
# Algorithm from https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
def gcd(a, b):

    if not isinstance(a, int) or not isinstance(b, int):
        return None
    # end if

    while b:
        a, b = b, a%b
    # end while

    return a

# end def


# MAAAIIINNNNN
if __name__ == "__main__":

    x = -4
    y = 72
    print "Greatest common divisor between " + str(x) + " and "+ str(y) + " is " + str(gcd(x,y))


# end main


