#!usr/bin/env python

# File:             filters.py
# Author:           Brad Anderson
# Date:             January 26, 2018
# File:             ME499 Lab2 - 
# Description:      
# Collaborators:    Nicole Guymer


from null_filter import *
import matplotlib.pyplot as plt
import copy


def mean_filter(rawData, n=3):
    
    if len(rawData) <= n:
        return rawData
    # end if

    filtered = copy.copy(rawData)

    







    for i,e in enumerate(rawData):
        if i == 0:
            filtered[0] = (rawData[0] + rawData[1])/2
        elif i == len(rawData)-1:
            filtered[-1] = (rawData[-1] + rawData[-2])/2
        else:
            filtered[i] = (e + rawData[i-1] + rawData[i+1])/3
        # end if
    # end for

    return filtered
# end def


# MAAAIIINNNNN
if __name__ == "__main__":

    data = generate_sensor_data()
    
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(data)
    ax2.plot(mean_filter(data))
    plt.show()

# end main


