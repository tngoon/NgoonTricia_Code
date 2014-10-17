#check_unnorm_TN.py
"""
This script sequentially opens unnormalized functional images for each subject and session within a subject and session list. User will then be prompted to input a rating of 1-3 for each image as well as notes for easy input in the database. 

Authored for Stanford Cognitive & Systems Neuroscience Laboratory
"""

import os
import csv
from subprocess import call

# Edit name of file containing list of subjects
subfile = open("test.txt",'r')
sublist = subfile.read().split('\n')
del sublist[-1]

# Edit name of file containing list of sessions
sessionfile = open("testsession.txt", 'r') #edit name of session list file
sessionlist = sessionfile.read().split('\n')
del sessionlist[-1]

# Edit CSV file name if you'd like
w = csv.writer(open('Unnorm_Ratings', 'wb'))

# Iterates through each task in your sessionlist for each subject in your subjectlist 	
for subject in sublist:
	for task in sessionlist:
		# Specifies which image to display		
		filename = '/fs/musk1/20%s/%s/fmri/%s/unnormalized/I.nii.gz' % (subject[0:2], subject, task)
		
		call(['fslview', filename])
		print subject, filename
		rating = raw_input("Rate from 1-3 (1 being worst, 3 being best):  ")
		notes = raw_input("Add notes for %s unnormalized:  " % (subject))

		w.writerow([subject, task, rating, notes])
