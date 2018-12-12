##script to create random dataset with given variables

#load packages
import pandas as pd 
import numpy as np 

###PARAMETERS###
#how many participants
pids = list(range(40))
#list IVs
conditions = ['H','C']
#list DVs
columns = ['condition', 'novelty', 'elaboration', 'feasibility', 'overall']

###MAKE THE RANDOM SAMPLE###

#make the empty dataframe w/ participants and DVs as columns
df = pd.DataFrame(index=pids, columns=columns)

#randomize DVs into condition
df['condition'] = np.random.choice(conditions, size=len(df), p=[.50,.50])

#add random numeric values for each DV
df['novelty'] = np.random.randint(1,4, size=(40,1))
df['elaboration'] = np.random.randint(1,4, size=(40,1))
df['feasibility'] = np.random.randint(1,4, size=(40,1))

print(df)

#export dataframe to csv
df.to_csv('scaffold_sim_data.csv')

