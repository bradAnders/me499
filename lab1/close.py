#!/usr/bin/env python

# Author:           Brad Anderson
# Date:             January 16, 2018
# File:             ME499 Lab0 difference comparison
# Description:      Checks if the difference between two numbers is less that a given threshold.
# Collaborators:    Kenzie Brian

from math import fabs


def close(a, b, diff):

    if fabs(a-b) < diff:
        return True
    else:
        return False
    # end if

# end close
if __name__ == '__main__':

    print close(1, 2, 3)
