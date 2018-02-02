#!/usr/bin/env python

# File:             filters.py
# Author:           Brad Anderson
# Date:             January 26, 2018
# File:             ME499 Lab2 - 
# Description:      
# Collaborators:    Nicole Guymer


from null_filter import *
import matplotlib.pyplot as plt
import copy
from numpy import median


def mean_filter(rawData, n=3):
    
    # Doesn't make sense for full-width filtering
    if len(rawData) <= n:
        return rawData
    # end if

    # Even filter widths not compatible
    if not(n % 2):
        print "Enter an odd number"
        return rawData
    # end if

    d_i = int((n-1)/2)

    filtered = copy.deepcopy(rawData)

    for i,e in enumerate(rawData):
        if i < d_i:
            # Forward filter at beginning
            filtered[i] = sum(rawData[i:i+(int(n)-1)])/n
        
        elif i >= len(rawData)-(d_i+1):
            # Backward filter at end
            filtered[i] = sum(rawData[i-(int(n)-1):i])/n
        
        else:
            # Normal case
            filtered[i] = sum(rawData[i-d_i:i+d_i+1])/n
        
        # end if
    # end for

    return filtered
# end defi


def median_filter(rawData, n=3):

    # Doesn't make sense for full-width filtering
    if len(rawData) <= n:
        return rawData
    # end if

    # Even filter widths not compatible
    if not(n % 2):
        print "Enter an odd number"
        return rawData
    # end if
   
    d_i = int((n-1)/2)

    filtered = copy.deepcopy(rawData)

    for i,e in enumerate(rawData):
        if i < d_i:
            # Forward filter at beginning
            subList = rawData[i:i+(int(n)-1)]
        
        elif i >= len(rawData)-(d_i+1):
            # Backward filter at end
            subList = rawData[i-(int(n)-1):i]
        
        else:
            # Normal case
            subList = rawData[i-d_i:i+d_i+1]
        
        # end if

        filtered[i] = median(subList)

    # end for

    return filtered
# end def


# MAAAIIINNNNN
if __name__ == "__main__":

    n = 33
    data = generate_sensor_data()
    d_mean = mean_filter(data, n)
    d_medn = median_filter(data, n)

    # Calculate differnce b/n mean & median
    d_diff = [0] * len(data)
    try:
        for i,e in enumerate(data):
            d_diff[i] = d_mean[i] - d_medn[i]
    except:
        print "Could not caluculate difference"
        d_diff = data[:]
    
    # Save to files
    print_sensor_data(data, "filter_raw")
    print_sensor_data(d_mean, "filter_mean")
    print_sensor_data(d_medn, "filter_median")
    
    # Figure with three subplots
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=False)
    ax1.plot(d_diff)
    ax1.set_title("Raw Data")
    ax2.plot(d_mean)
    ax2.set_title("Neighbor mean with n = %d" % n)
    ax3.plot(d_medn)
    ax3.set_title("Median filter with n = %d" % n)
    plt.show()



# end main


