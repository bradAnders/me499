#!/usr/bin/env python

# File:             sinPlot.py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators:    


import matplotlib.pyplot as plt
import numpy as np
import math


# plots a sin function
def sinPlot():

    # (start, stop, count)
    time = np.linspace(0, 4*math.pi, 1000)
    
    plt.plot(time, map(math.sin,time))
    plt.axis([1, 4*math.pi, -1, 1])
    plt.xlabel('x')
    plt.ylabel('y = sin(x)')
    plt.title('A sin wave!')
    plt.show()

# end def


# MAIN
if __name__ == "__main__":

    sinPlot()

# end main


