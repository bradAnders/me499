#!usr/bin/env python

# Author:           Brad Anderson
# Date:             January 32, 2018
# File:             ME499 Lab2 - iterative and recursive reverse
# Description:      Reverses a list of numbers with both a recursive
#                   and an iterative method
# Collaborators:    Kenzie Brian


import copy


# Reverses a list iteratively
def reverse_i(nums_in):

    numbers = copy.copy(nums_in)

    n = len(numbers)
    print str(n) + " numbers"
    
    for i in range((n/2)):
        print "i = " + str(i)

        # Swap mirrored indicies
        temp = numbers[i]
        numbers[i] = numbers[n-1-i]
        numbers[n-1-i] = temp
        
    # end for

    return numbers

# end def


# Reverses a list recursively
def reverse_r(nums_in):

    n = len(nums_in)
    
    # End case
    if n < 2:
        return nums_in
    # end if

    # Swap first and end entries, and then reverse list[1:n-1]
    # Concatenate them in the return
    return [nums_in[n-1]] + reverse_r(copy.copy(nums_in[1:n-1])) + [nums_in[0]]

# end def
    

# MAINNNNN
if __name__ == "__main__":

    nums = [3, 2, 5, -1, 77, -3, 0, 31, 0]
    print "Original list is " + str(nums)
    print "Iterative reverse is " + str(reverse_i(nums))
    print "Recursive reverse is " + str(reverse_r(nums))

# end main


