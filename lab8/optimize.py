#!/usr/bin/env python

# File:             optimize.py
# Author:           Brad Anderson
# Date:             March 9, 2018
# Project:          ME 499, Lab 8
# Description:      Finds maximums of single variate fuctions
#                   with multiple methods and compares them
#                   Also finds the maximum of a multivariate function
# Collaborators:    Nicole Guymer
# Sources Used:     
#   -- Overflow Error --
#   https://stackoverflow.com/questions/7559595/python-runtimewarning-overflow-encountered-in-long-scalars


from subprocess import call
import sys
import numpy as np
from random import uniform
from scipy import optimize
import matplotlib.pyplot as plt
from copy import copy


def optimize_step(f, bounds, n):
    (x0, xf) = bounds

    # linspace is number of points, not steps
    x_array = np.linspace(x0, xf, n+1)

    # Calculate all values of y for x values
    y_array = [f(x) for x in x_array]

    # Find where the max is
    i_max = np.argmax(y_array)

    # Return the corresponding x
    return x_array[i_max]


def optimize_random(f, bounds, n):
    (x0, xf) = bounds

    # Create array of random x values and sort them
    # Sorted array might make argmax run faster
    x_array = sorted([uniform(x0,xf) for i in xrange(n)])
    y_array = [f(x) for x in x_array]
    
    # Find where max is
    i_max = np.argmax(y_array)

    # Return that corresponding x value
    return x_array[i_max]


def optimize_gradient(f, bounds, epsilon):
    (x0, xf) = bounds

    # Set a default amount to vary guesses
    dx = abs(xf-x0)/10.0

    # Initialize variables for while loop
    x1 = uniform(x0, xf)
    x2 = x1 + dx
    y1 = f(x1)
    y2 = f(x2)

    # Figure out which way the gradient points
    if f(x2) > f(x1):
        pos_slope = True
    else:
        pos_slope = False

    # Follow the gradient until within error
    while ( abs(y2 - y1) > epsilon ):

        # Set the new guess based on slope direction
        # If new guess is outside bounds, then max is a bound
        if pos_slope:
            x2 = x1+dx
            if x2 >= xf:
                return float(xf)
        else:
            x2 = x1-dx
            if x2 <= x0:
                return float(x0)

        # Calculate values at guesses
        y1 = f(x1)
        y2 = f(x2)

        # If new guess passed over the maximum,
        # then turn around and refine precision
        if y2 < y1:
            dx = dx/2.0
            pos_slope = not pos_slope
        
        # Starting point for next loop
        x1 = x2

    # When while loop ends, last value set to x1 is maximum
    return x1


def optimize_md(f, bounds):

    # Initialize loop variables
    # Tried convert as much to np.float64 as possible, but 
    # overflow error will not go away
    num_its = 1000
    out_y = np.array([],dtype=np.float64)
    test_x = np.array([np.array([None for j in xrange(len(bounds))],
        dtype=np.float64) for i in xrange(num_its)], dtype=np.float64)
    test_y = np.array([None for i in xrange(num_its)], dtype=np.float64)

    # Try a ton of guesses and pick the maximum
    for i in xrange(num_its):

        # Pick guess within bounds of j-th dimension
        for j, (low, hi) in enumerate(bounds):
            test_x[i,j] = uniform(low, hi)
        
        # Evaluate function at test points
        test_y[i] = f(*test_x[i])
    
    # Pick maximum of that function
    max_i = np.argmax(test_y)
    close_guess = test_x[max_i]
    exact = close_guess.copy()
    
    # Now that we have close guesses, use optimizer to fine tune
    # Create lambda functions to evaluate multivariate fun
    # one dimension at a time
    for i, (low, hi) in enumerate(bounds):
        if i == 0:
            one_dim_fun = lambda x: -f(*np.array(
                [x]+list(exact[1:]),
                dtype=np.float64))
        elif i == len(bounds)-1:
            one_dim_fun = lambda x: -f(*np.array(
                list(exact[:-1])+[x],
                dtype=np.float64))
        else:
            one_dim_fun = lambda x: -f(*np.array(
                list(exact[:i])+[x]+list(exact[i+1:]),
                dtype=np.float64))
        
        # Grab the minimum in the i-th dimension and save it
        # for the other dimensions
        exact[i] = optimize.minimize_scalar(one_dim_fun).x

    return exact


def quad(x):
    return -x**2.0

def multi(x,y,z):
    return -(x)**2.0 + -(y-1)**2.0 + z


# MAIN
if __name__ == "__main__":

    sys_args = sys.argv

    #call(["clear"])

    errors = []
    iterations = range(2,100)
    bounds = (-50, 50)
    test_fun = quad
    for i in iterations:

        s = optimize_step(test_fun, bounds, i)
        r = optimize_random(test_fun, bounds, i)
        g = optimize_gradient(test_fun, bounds, float(i)**(-2))
        o = optimize.minimize_scalar(lambda x: -test_fun(x)).x
        errors.append( (s,r,g,o) )

    plt.plot(iterations, [s for (s,r,g,o) in errors])
    plt.plot(iterations, [r for (s,r,g,o) in errors])
    plt.plot(iterations, [g for (s,r,g,o) in errors])
    plt.plot(iterations, [o for (s,r,g,o) in errors])
    plt.legend(["Step", "Random", "Gradient", "SciPy" ])

    bounds_md = [(-10, 10), (-10, 10), (-10, 10)]
    #bounds_md = [(-10, 10)]
    m = optimize_md(multi, bounds_md)
    print m

    plt.show()

# end main


