#!/usr/bin/env python

# File:             lab3.py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators:    


from sinPlot import sinPlot
from randomPlot import randomPlot
from msdPlot import msdPlot
from plotTimes import plotTimes, randomList

from math import pi


# MAIN
if __name__ == "__main__":

    #sinPlot(0, 4*pi)
    #randomPlot(n=10000, sum_n=10)
    #msdPlot(m=50.0, k=5.0, c=5.0, x=-20.0, xD=15.0)

    # My Chromebook can't handle list length >10e4, so this is untested
    functionsToTest = [sorted, sum]
    plotTimes(funs=functionsToTest, base=10, n_0=0, n=3)


# end main


