#script to randomly sample dataset into subsets and create an overlap sample to include for each subset

#load packages
import pandas as pd 
import numpy as np 

data = pd.DataFrame(pd.read_csv("combined_data_nodups.csv"))

#subset into the different courses
f16 = data.loc[data['Course']=="F16"]
w17 = data.loc[data['Course']=="W17"]
courses = [f16, w17]

randsamp = pd.DataFrame()
for course in courses:
    course['subset'] = np.random.choice([1,2,3,4], size=len(course), p=[.25,.25,.25,.25])
    a = course.sample(frac=0.30) #30% from each course
    temp = pd.DataFrame({'ID':a.ID, 'Comment': a.Comment, 'Course': a.Course,'subset':a.subset})
    #create random sample
    randsamp = pd.concat([randsamp, temp])
    randsamp.to_csv('random_sample.csv')
#create overlap sample
overlap = randsamp.sample(frac=0.10) #10% of the original 
overlap.to_csv('overlap_sample.csv')

subsets = [1,2,3,4]
for subset in subsets:
 	#new dataframe for each subset
 	b = randsamp.loc[randsamp['subset']== subset]
 	#add overlap sample to each subset
 	df = pd.concat([b, overlap])
 	#drop duplicates
 	df.drop_duplicates()
 	df.to_csv('subset_%s.csv' %subset)
