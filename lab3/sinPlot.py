#!/usr/bin/env python

# File:             sinPlot.py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators:    


import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin


# plots a sin function
def sinPlot(s=0.0, e=2*pi, c=100):

    # (start, end, count)
    time = np.linspace(s, e, c)
    
    plt.plot(time, map(sin,time))
    plt.axis([s, e, -1, 1])
    plt.xlabel('x')
    plt.ylabel('y = sin(x)')
    plt.title('A {0:.2}-wavelength sin wave!'.format((e-s)/(2*pi)))
    plt.show()

# end def


# MAIN
if __name__ == "__main__":

    sinPlot()

# end main


