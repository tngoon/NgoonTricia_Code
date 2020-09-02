##script to create random dataset with given variables

#load packages
import pandas as pd 
import numpy as np 

###PARAMETERS###
#how many participants
pids = list(range(24))
#list IVs
conditions = ['w','c']
#list DVs
columns = ['condition', 'visual clarity', 'visual creativity', 'narrative clarity', 'narrative creativity', 'overall']

###MAKE THE RANDOM SAMPLE###

#make the empty dataframe w/ participants and DVs as columns
df = pd.DataFrame(index=pids, columns=columns)

#randomize DVs into condition
df['condition'] = np.random.choice(conditions, size=len(df), p=[.50,.50])

#add random numeric values for each DV
df['visual clarity'] = np.random.randint(0,5, size=(24,1))
df['visual creativity'] = np.random.randint(0,5, size=(24,1))
df['narrative clarity'] = np.random.randint(0,5, size=(24,1))
df['narrative creativity'] = np.random.randint(0,5, size=(24,1))
df['overall'] = np.random.randint(0,5, size=(24,1))

#export dataframe to csv
df.to_csv('comic_sim_data.csv')

