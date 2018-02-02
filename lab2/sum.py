#!/usr/bin/env python

# File:             sum.py
# Author:           Brad Anderson
# Date:             January 32, 2018
# File:             ME499 Lab2 - iterative and recursive sum
# Description:      Sums a list of numbers with both a recursive
#                   and an iterative method
# Collaborators:    Kenzie Brian


# Sums a list iteratively
def sum_i(numbers):

    sum = 0
    
    for num in numbers:
        sum += num
    # end for

    return sum

# end def


# Sums a list recursively
def sum_r(numbers):

    if len(numbers) == 0:
        return 0
    # end if

    return numbers[0] + sum_r(numbers[1:])

# end def
    

# MAAAIIINNNNN
if __name__ == "__main__":

    nums = [3, 2, 5, -1, 77, -3, 0, 32, 31, 0]
    print "Iterative sum is " + str(sum_i(nums))
    print "Recursive sum is " + str(sum_r(nums))

# end main


