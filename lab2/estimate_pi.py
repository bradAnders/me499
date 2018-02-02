#!/usr/bin/env python

# File:             estimate_pi.py
# Title:            ME499 Lab2 - Estimating Pi
# Author:           Brad Anderson
# Date:             January 32, 2018
# Description:      Exercise 7.5
# Collaborators:    Kenzie Brian

from math import *
from decimal import Decimal

# estimates pi
def estimate_pi():

    pi_inv = 2*(2.0**(0.5))/9801.0

    k = 0.0
    new_coeff = 1
    pi_sum = 0;
    while (new_coeff >= 1e-15):
        num = factorial(4*k)*(1103 + 26390*k)
        den = (factorial(k)**4)*(396**(4*k))
        new_coeff = num/den
        pi_sum += new_coeff
        k += 1
    # end while

    #return pi_inv
    return 1/(pi_inv*pi_sum)

# end def


# MAAAIIINNNNN
if __name__ == "__main__":

    print "Pi estimation: %.50g" % estimate_pi()
    print "Official pi:   %.50g" % pi
    print "Difference from math.pi is %.9g" % (pi-estimate_pi())

# end main


