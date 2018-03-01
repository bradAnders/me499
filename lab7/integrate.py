#!/usr/bin/env python

# File:             integrate.py
# Author:           Brad Anderson
# Date:             March 1, 2018
# Project:          ME 499, Lab 7
# Description:      Contains functions for integrating
#                   with Riemann sum and Monte Carlo integration
# Collaborators:    None
# Sources Used:     
#   -- Check if object is number --
#   https://stackoverflow.com/questions/4187185/how-can-i-check-if-my-python-object-is-a-number

import numpy as np
from random import uniform as rand
from math import pi, sin, acos
import matplotlib.pyplot as plt
from copy import copy


# Basic Trapezoid rule Riemann Sum
def integrate(f, a, b, n=100):

    # Argument checks
    for e in (a,b):
        if not isinstance(e, (int, long, float)):
            raise TypeError
    check_n(n)

 
    x_vals = np.linspace(float(a), float(b), num=n)
    del_x = x_vals[1]-x_vals[0]
    y_sum = 0.0

    # Shorten index by one to prevent OB error
    for i in xrange(len(x_vals)-1):
        try:
            # Trapeziodal Riemann sum
            y_sum += del_x*( f(x_vals[i])+f(x_vals[i+1]) )/2.0
        except:
            raise ValueError
    return y_sum



# Monte Carlo geussing-method for integration
def integrate_mc(f, a, b, (c, d), n=100):
    
    # Argument checks
    for e in (a,b,c,d):
        if not isinstance(e, (int, long, float)):
            raise TypeError
    check_n(n)

    count = 0
    for i in xrange(n):
        x_i = rand(a,b)
        y_i = rand(c,d)

        # Take into account function crossing x-axis
        if y_i > 0:
            # if guess is b/n fcn & x-axis, count up
            if y_i <= f(x_i):
                count += 1
        else:
            if y_i >= f(x_i):
                count += 1

    # Integral is ratio of guesses times guessed area
    return (count / float(n)) * float(b-a) * float(d-c)


# Most basic linear funciton
def linear(x):
    return x


# Quadratic function with hardcoded coefficients
def quad(x):
    return 1.0*(x**2) + 1.0*(x) + 1.0


# Function for a hemisphere centered at 0,0, with argument for
# top of bottom half return values
def circle(x, positive=True):
    radius = 1.0
    if x > radius or x < -radius:
        return None
    if positive:
        return sin(acos(abs(x)))
    else:
        return -sin(acos(abs(x)))


# Check if number of guesses is int and if is positive
def check_n(n):
    if not isinstance(n, (int, long)):
        raise TypeError
    if n<=0:
        raise ValueError
    return


# Use Monte Carlo integration to calculate pi
def approximate_pi(n):
    # Integrate top half of circle and multiply by 2
    return integrate_mc(circle,-1.0,1.0,(1.0,0.0),n)*2.0


# MAIN
if __name__ == "__main__":

    a = 0.0
    b = 1.0
    c = -10.2
    d = 15
    f = quad
    n_range = [10**(i+1) for i in xrange(6)]

    # Pre-populate arrays
    ans_Riemann = [None for i in xrange(len(n_range))]
    err_Riemann = list(ans_Riemann)
    ans_MonteCarlo = list(ans_Riemann)
    err_MonteCarlo = list(ans_MonteCarlo)

    # Closed form integral for above quadratic function
    ans_closed_form = ((b-a)**3)/3.0 + ((b-a)**2)/2.0 + (b-a)
    
    # Calculate approimations and errors from closed-form solution
    for i,n in enumerate(n_range):
        ans_Riemann[i] = integrate(f, a, b, n)
        err_Riemann[i] = ans_Riemann[i] - ans_closed_form

        ans_MonteCarlo[i] = integrate_mc(f, a, b, (c, d),n)
        err_MonteCarlo[i] = ans_MonteCarlo[i] - ans_closed_form

    # Print pi
    print 'Monty  pi:', approximate_pi(n_range[-1]) 
    print 'Python pi:', pi


    # -- PLOTS --
    plt.plot()

    plt.subplot(121)
    #plt.semilogx(n_range, err_Riemann,'o')
    plt.loglog(n_range, err_Riemann)
    plt.grid()
    plt.xlabel('Abolute error')
    plt.ylabel('Number of bins')
    plt.title('Riemann Sum Approximation')

    # My Celeron processor has a hard time with graphics,
    # so sometimes the log-log doesn't scale properly.
    # I added options for debugging this.
    plt.subplot(122)
    #plt.semilogx(n_range, err_MonteCarlo,'o')
    #plt.semilogx(n_range, err_MonteCarlo)
    plt.loglog(n_range, err_MonteCarlo)
    plt.grid()
    plt.xlabel('Abolute error')
    plt.ylabel('Number of guesses')
    plt.title('Monte Carlo Approximation')

    plt.show()

# end main


