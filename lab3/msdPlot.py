#!/usr/bin/env python

# File:             .py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators:    
# Sources Used:
#   -- Subplots --
#   https://matplotlib.org/examples/pylab_examples/subplots_demo.html


from msd import MassSpringDamper
import matplotlib.pyplot as plt


def msdPlot(m=10.0, k=10.0, c=1.0, x=0.0, xD=1.0 ):

    mass = m
    springK = k
    dampingC = c
    xInitial = x
    xDotInitial = xD
    smd = MassSpringDamper(m=mass, k=springK, c=dampingC)

    a_state, a_time = smd.simulate(xInitial, xDotInitial)

    fig, a_axes = plt.subplots(2, sharex=True)
    a_axes[0].plot(a_time, a_state[:,0])
    a_axes[0].set_ylabel('Position')
    a_axes[0].grid()
    a_axes[1].plot(a_time, a_state[:,1])
    a_axes[1].set_ylabel('Velocity')
    a_axes[1].grid()
    
    plt.xlabel('Time')
    title = 'Mass Spring Damper with m={0}, k={1}, c={2}'
    subtitle = 'Initial position of {3} and velocity of {4}'
    plt.suptitle(
            (title + '\n' + subtitle).format(
                mass,
                springK,
                dampingC,
                xInitial,
                xDotInitial))
    plt.show()

# end def



# MAIN
if __name__ == "__main__":

    msdPlot()

# end main


