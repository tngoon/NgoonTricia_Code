#script to randomly sample dataset into subsets and create an overlap sample to include for each subset

#load packages
import pandas as pd 
import numpy as np 

####PARAMETERS###
#load data
data = pd.DataFrame(pd.read_csv("restaurant.csv"))
# a3_3 = data.loc[data['assignment']=="a3.3"]
# a3_4 = data.loc[data['assignment']=="a3.4"]
# a4_1 = data.loc[data['assignment']=="a4.1"]
# a4_2 = data.loc[data['assignment']=="a4.2"]
# assignments = [a3_3, a3_4, a4_1, a4_2]

# randsamp = pd.DataFrame()

#create 2 subsets
data['subset'] = np.random.choice([1,2], size =len(data), p=[.50,.50])

# for assignment in assignments:
#     assignment['subset'] = np.random.choice([1,2,3,4], size=len(data.assignments), p=[.25,.25,.25,.25])
#     a = assignment.sample(frac=0.50) #50% from each assignment for each subset
#     temp = pd.DataFrame({'Comment': a.comment, 'assignment': a.assignment,'subset':a.subset})
#     #create random sample
#     randsamp = pd.concat([randsamp, temp])
#     randsamp.to_csv('../data/cogs160/random_sample.csv')

#of the random sample, create overlap sample for all raters
overlap = data.sample(frac=0.25) #25% of the original random sample
overlap.to_csv('overlap_sample.csv')

subsets = [1,2]
for subset in subsets:
 	##new dataframe for each subset
 	b = data.loc[data['subset']== subset]
 	##add overlap sample to each subset
 	df = pd.concat([b, overlap])
 	##drop duplicates
 	df.drop_duplicates()

 	##shuffle rows of dataframe
 	ds = df.sample(frac=1)
 	ds.to_csv('subset_%s.csv' %subset)
