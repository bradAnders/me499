#!/usr/bin/env python

# File:             random.py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators:

#import matplotlib.pyplot as plt
from random import random


def randomSum(start=0, end=1, n=10):
    return sum([random() for e in xrange(n)])
# end def


def randomPlot(n=10000, sum_n=10):

    l_random = [randomSum(n=n) for e in xrange(n)]

    print sum(l_random)

    #pyplot.plot(l_random)
    #pyplot.show()

# end def


# MAIN
if __name__ == "__main__":

    randomPlot()

# end main


