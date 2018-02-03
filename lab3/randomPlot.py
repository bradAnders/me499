#!/usr/bin/env python

# File:             random.py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators:

import matplotlib.pyplot as plt
from random import uniform


def randomSum(s=0.0, e=1.0, n=10):
    return sum([uniform(start, end) for e in xrange(n)])
# end def


def randomPlot(n=10000, s=0.0, e=0.0, sum_n=10):

    l_random = [randomSum(s=s, e=e, n=sum_n) for e in xrange(n)]

    xlabel = 'Value of summing {0} numbers from {1} to {2}'
    plt.hist(l_random)
    plt.xlabel(xlabel.format(sum_n, 0, 1))
    plt.ylabel('Number of occurances in bin width')
    plt.title('Histogram of Random Set of Sums')
    plt.show()

# end def


# MAIN
if __name__ == "__main__":

    randomPlot(n=10000, sum_n=10)

# end main


