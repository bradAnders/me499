#!/usr/bin/env python

# File:             simulator.py
# Author:           Brad Anderson
# Date:             March 7, 2018
# Project:          ME 499, Homework 2
# Description:      Runs a simulator with a set of data points
# Collaborators:    None
# Sources Used:
#   -- Calling Shell Commands --
#   https://stackoverflow.com/questions/89228/calling-an-external-command-in-python
#   -- Getting Shell Outputs --
#   http://www.pythonforbeginners.com/os/subprocess-for-system-administrators
#   -- Getting Shell Arguments --
#   https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/

import subprocess
import sys
from random import randint
import numpy as np

class simulator:
    def __init__(self, problem):
        self.problem = problem
        return

    def evaluate(self, waypoints):
        self.save_waypoints(waypoints)
        call = ["./simulator-linux"]
        args = ["__test_waypoints", str(self.problem)]

        # Call simulator in shell and capture output
        output_string = subprocess.Popen(
                call+args, 
                stdout=subprocess.PIPE)
        # Pass output to another method to get result
        test_output = self.getResult(output_string)
        return test_output

    # Save path under test to a special file so the simulator
    # can access it
    def save_waypoints(self, waypoints, name="__test_waypoints"):
        with open(name,"w") as f:
            for (x, y) in waypoints:
                f.write(str(x) + " " + str(y) + "\n")
        return

    # Convert lines of text to list of words. Assume result
    # is the second to last word in the output
    def getResult(self, output_string):
        words = []
        for line in output_string.communicate():
            for word in str(line).strip().split():
                words.append(word)
        # Remove period from end of word so it is a valid float
        return float(words[-2][0:-2])


# Get simulation number from shell call
def get_sim_number(default=10):
    sys_args = sys.argv
    try:
        sim_num = float(sys_args[1])
    except:
        return default
    return sim_num


# The most basic path improvement algorithm
def improve_path(old_path, sim):

    new_path = old_path[:]

    # Catch bad input
    if len(old_path) <= 1:
        new_path = [(-10, -10), (10, 10)]

    # Create a new node somewhere randomly in the path.
    # New node is on old path, halfway between its neighbors
    new_index = randint(1, len(new_path)-1)
    start = new_path[new_index-1]
    end   = new_path[new_index]
    new_node = ((start[0]+end[0])/2.0, (start[1]+end[1])/2.0)
    new_path.insert(new_index, new_node)

    # Get a reference for how good the last path was
    old_result = sim.evaluate(new_path)

    # Try out a few directions and see which one is best
    tests = []
    directions = ["n", "s", "e", "w"]
    for d in directions:
        test_path = vary_waypoint(new_path, new_index,d=d)
        tests.append(sim.evaluate(test_path))
    best_dir = np.argmin(tests)

    # For this simple example, just return a small variation
    return vary_waypoint(new_path, new_index, d=directions[best_dir])


# Return a path with the specified variation
def vary_waypoint(path, index, d="n", dx=0.1, dy=0.1):

    (wx, wy) = path[index]
    copy = path[:]
    if d == "n":
        copy[index] = (wx, wy+dy)
    elif d == "s":
        copy[index] = (wx, wy-dy)
    elif d == "e":
        copy[index] = (wx+dx, wy)
    elif d == "w":
        copy[index] = (wx-dx, wy)
    
    return copy


# MAIN
if __name__ == "__main__":

    # Clear the terminal
    #subprocess.call(["clear"])

    sim_num = get_sim_number(default=1)

    w = [(-10, -10), (10, 10)]
    s = simulator(sim_num)

    new_path = improve_path(w, s)
    s.save_waypoints(new_path, name="better_waypoints")

    print "Radiation from problem", sim_num, ":", s.evaluate(w)
    print "Radiation from new path", ":", s.evaluate(new_path)
    print "Path taken:", new_path


# end main


