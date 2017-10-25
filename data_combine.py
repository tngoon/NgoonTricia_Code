#combine multiple csvs into a single csv

import numpy as py
import pandas as pd
import glob
import csv
import os
import sys

os.chdir("/Users/triciangoon/Desktop/F16")
cwd = ("/Users/triciangoon/Desktop/F16")

folders = os.walk(cwd).next()[1]

#make dataframe for combining spreadsheets
combine=pd.DataFrame([])

#add filename to each spreadsheet to separate by assignment and rubric item
for folder in folders:
	filenames = glob.glob(folder + "/.csv")

	for filename in filenames:
		writer = csv.writer(open(filname,'a'))
		writer.writerow([filename])
		df = pd.read_csv(filename, skiprows=0)
		combine.append(df)

	#combine spreadsheets from each folder together
	combine.to_csv('all_assignments.csv')
