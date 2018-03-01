#!/usr/bin/env python

# File:             roots.py
# Author:           Brad Anderson
# Date:             February 23, 2018
# Project:          ME 499, Lab 6
# Description:      
# Collaborators: 
# Sources Used:
#   -- Reason --
#   URL

from complex import Complex


def roots(a, b, c):

    real = -b/(2*a)
    
    square = (b*b) - (4*a*c)

    if square < 0:
        imag = Complex(0, ((-square)**(0.5)) / (2*a))
    else:
        imag = (square**(0.5)) / (2*a)
    # end if

    return (real-imag, real+imag)
# end def


# MAIN
if __name__ == "__main__":

    r1, r2 = roots(1, 6, 9)
    print r1
    print r2

# end main


