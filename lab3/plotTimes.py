#!/usr/bin/env python

# File:             plotTimes.py
# Author:           Brad Anderson
# Date:             February 2, 2018
# Project:          ME499 Lab3
# Description:      
# Collaborators: 
# Sources Used:
#   -- timeit use --
#   https://docs.python.org/2/library/timeit.html


from random import uniform
from timeit import timeit
import matplotlib.pyplot as plt


def randomList(s=0.0, e=1.0, n=1):
    return [uniform(s, e) for e in xrange(n)]

def timeFunction(function, base=10, n_0=0, n=2):

    ll_times = [[0 for c in xrange(2)] for r in xrange(n+n_0)]
    for exp in xrange(n_0, n+n_0):
        ll_times[exp][0] = int(base**exp)
        ll_times[exp][1] = timeit(
            '{}(l_random)'.format(function.__name__),
            setup=(
                'from __main__ import randomList;' +
                'l_random=randomList(n=int({0}**{1}));'
                .format(base, exp) +
                'print "{0}(): {1} element(s)...".format(len(l_random))'
                .format(function.__name__,"{0}")))
        print ' --> Took {0:.4}s\n'.format(ll_times[exp][1])
    # end for

    return ll_times
# end def


def plotTimes(funs=[sum, sorted], base=3, n_0=0, n=3):

    count = len(funs)

    times = [None for i in xrange(count)]
    for i, function in enumerate(funs):
        times[i] = timeFunction(function, base=base, n_0=n_0, n=n)
    # end for

    figure, a_axes = plt.subplots(count, sharex=True)

    for i, function in enumerate(funs):
        a_axes[i].plot(
                [e[0] for e in times[i]],
                [e[1] for e in times[i]])
        a_axes[i].set_ylabel('Time to return')
        a_axes[i].set_title('Timing the "{}()" Function'
                .format(function.__name__))
    plt.xlabel('Number of elements in list')
    plt.show()
    
# end def


# MAIN
if __name__ == "__main__":

    plotTimes(base=3, n_0=0, n=3)

# end main


