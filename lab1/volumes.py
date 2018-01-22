#!/usr/bin/env python

# Author:           Brad Anderson
# Date:             January 16, 2018
# File:             ME499 Lab0 volume calculation
# Description:      Calculates the volume of a torus and a cylinder
# Collaborators:    Kenzie Brian

from math import pi


def cylinder_volume(radius, height):

    if radius < 0 or height < 0:
        return None
    # end if

    return height * (pi * radius**2)

# end cylinder_volumes


def torus_volume(major, minor):

    if major < 0 or minor < 0:
        return None
    # end if

    return 2 * pi**2 * major * minor**2

# end torus_volumes


if __name__ == '__main__':

    print cylinder_volume(3, 4)

    print torus_volume(7, 3)
