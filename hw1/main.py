#!/usr/bin/env python

# File:             main.py
# Author:           Brad Anderson
# Date:             February 16, 2018
# Project:          Homework 1
# Description:      
# Collaborators: 
# Sources Used:
#   -- Finding 'lab' in dictionary --
#   https://stackoverflow.com/questions/43332688/finding-all-occurrences-of-a-word-in-a-dictionary-of-lists
#   -- Calling dictionary in reverse --
#   http://drumcoder.co.uk/blog/2010/sep/11/find-key-value-python-dictionary/


import csv
import numpy as np


# Each student has an object which contains their grades and ID
class Student():
    ident = 0
    grades = []

    def __init__(self, grades=[], ident=0):
        self.ident = ident
        self.grades = grades

    def __str__(self):
        try:
            return str(
                    'ID ' +
                    str(self.ident) +
                    ': ' +
                    str(self.grades[-1]) +
                    '%')
        except:
            return 'Uninitialized student'

    # Assume last column in CSV is final grade
    def total(self):
        return self.grades[-1]

    # Hardcode that homeworks are in columns 46:56
    def homework(self,number=0):
        if number==0:
            return np.average(self.grades[46:56])
        else:
            return self.grades[46+number]

    # Access specific grades based on index
    def grade(self, number):
        return self.grades[number]
# end class


def read_csv_to_matrix(filepath):
    file_contents = []
    with open (filepath, 'r') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(file_reader):
            temp_row = []
            for element in row:
                try:
                    temp_row.append(float(element))
                except:
                    # First row is titles; convert NaNs elsewhere to 0
                    if i == 0:
                        temp_row.append(element)
                    else:
                        temp_row.append(0.0)
            file_contents.append(temp_row)
        # end for
    # end with
    return file_contents
# end def


def print_class_averages(students):

    above_avg = 0
    above_med = 0
    finals = []

    # Grab list of all the final grades
    for i,e in enumerate(students):
        finals.append(e.total())

    average = np.average(finals)
    median = np.median(finals)

    # Count how many are above average and median
    for i,e in enumerate(students):
        if e.total() > average:
            above_avg += 1
        if e.total() > median:
            above_med += 1

    # Convert to percentage
    abv_avg_per = above_avg*100.00/len(students)
    abv_med_per = above_med*100.00/len(students)

    print 'Average Score:{:.2f}'.format(average)
    print 'Above Average: {:0.2f}%'.format(abv_avg_per)
    print 'Median Score:{:.2f}'.format(median)
    print 'Above Median: {:0.2f}%'.format(abv_med_per)

# end def


def print_hardest_assignment(students, dictionary):

    # Hardcode where homeworks are
    # Wrote 'find_idx_if_contains' later,
    # which finds the index of grades with a string in the title,
    # such as all "homework" grades
    hw_start = 46
    num_hw = 11
    hw_indices = range(hw_start, hw_start+num_hw)

    averages = get_averages_for_indices(students, hw_indices, normalized=True)

    # find the index of the hardest number
    hard_hw_num = np.argmin(averages)

    # grab the title from the dictionary
    title = dict_rev(dictionary, hard_hw_num+hw_start)

    print 'Hardest Assignment: {}'.format(title)
# end def




def get_averages_for_indices(students, indices, normalized=False):

    scores = [[] for i in xrange(len(indices))]
    averages = []

    # pull all scores from these columns
    for student in students:
        for j,e in enumerate(indices):
            scores[j].append(student.grade(e))
        # end for
    # end for

    # average lists of scores and return averages
    for j,e in enumerate(indices):
        averages.append(np.nanmean(scores[j]))
        if normalized:
            averages[-1] = averages[-1]/float(max(scores[j]))
        # end if
    # end for

    return averages
# end def


def print_hardest_labs(students, dictionary):

    # Find all the grades with 'lab ' in the title.
    # Using 'lab_' instead of 'lab' to filter out 'collaboration'
    # and 'Labs current score' and 'labs final score'
    lab_idx = find_item_if_contains(dictionary, 'lab ')
    averages = get_averages_for_indices(students, lab_idx, normalized=True)

    # harest lab is one with lowest score
    index = idx_of_lowest(averages)
   
    # grab the title from the dictionary
    title = dict_rev(dictionary, index)
    
    print 'Hardest Lab: {}'.format(title)

# end def


# Helper function to increase readability
def idx_of_lowest(list_to_search):
    return np.argmin(list_to_search)
# end def


# Find all the grades that have a given string in their title
def find_item_if_contains(dictionary, string):
    return [idx for (val, idx) in dictionary.items() if string in val.lower()]
# end def


# Find the title of the given grade index
def dict_rev(d, e):
    keys = [key for key, value in d.iteritems() if value == e]
    return keys[0]
# end def


def print_grading_distribution(students):
    
    final_grades = [s.total() for s in students]
    titles = ['A ','A-','B+','B ','B-','C+','C ','C-','D+','D ','D-','F ']
    count  = [  0,   0,   0,  0,   0,   0,  0,   0,   0,  0,   0,  0]
    thresh = [ 94,  90,  87, 84,  80,  77, 74,  70,  67, 64,  61,  0]
    for grade in final_grades:
        for i, thr in enumerate(thresh):
            if grade >= thr:
                count[i] += 1
                break
            # end if
        # end for
    # end for

    for i, e in enumerate(titles):
        print '{} {:2}'.format(e, count[i])
    # end for

# end def


def print_complaining_students(students):

    thresh = [ 94,  90,  87, 84,  80,  77, 74,  70,  67, 64,  61,  0]
    final_grades = [s.total() for s in students]

    complain_count = 0

    for grade in final_grades:
        for thr in thresh:
            diff = thr - grade
            if diff > 0 and diff <= 0.5:
                complain_count += 1
                break
            # end if
        # end for
    # end for

    print '{} students will complain about their grade.'.format(complain_count)

# end def


def print_new_cutoffs(students):

    final_grades = [s.total() for s in students]
    num_grades = len(final_grades)
    percent = [10, 20, 30, 30]
    grade_count = []
    for i in xrange(len(percent)):
        grade_count.append(int(round(num_grades * float(percent[i])/100)))
    # end for
    grade_count.append(num_grades - (sum(grade_count)))
   

    current_count = 0
    cutoffs = []
    for i in xrange(len(grade_count)-1):
        current_count += grade_count[i]
        cutoffs.append(
                sorted(final_grades, reverse=True)[current_count-1]
                )
    # end for
    
    for i,e in enumerate(['A','B','C','D']):
        print '{} {:5.2f}'.format(e, cutoffs[i])
    # end for

# end def


# MAIN
if __name__ == "__main__":

    grades_file = read_csv_to_matrix('./grades.csv')

    titles = grades_file[0]

    # Create dictionary to correlate grade type and index
    d = {}
    for i, title in enumerate(titles):
        d[title] = i
    
    # Populate array of Student objects
    students = []
    for i in xrange(1, len(grades_file)):
        students.append(Student(grades_file[i], i))

    print_class_averages(students)
    
    print_hardest_assignment(students, d)

    print_hardest_labs(students, d)

    print_grading_distribution(students)

    print_complaining_students(students)

    print_new_cutoffs(students)

# end main


