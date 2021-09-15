#!/usr/bin/env python3

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#this is the specific directory where the data we want to use is stored----CHANGE
datadirectory = '/Users/maria_hernandez/Desktop/intro_coding_mh/data/'

#this is the directory where we want to store the data we finish analyzing---------CHANGE
data_out_directory='/Users/maria_hernandez/Desktop/intro_coding_mh/output/'

#read_in data
temp_data=pd.read_csv(datadirectory+'Temp_data_2010-2020.csv')

#select a wanted lake
lake_wanted=sys.argv[1]

lake_subset=temp_data.loc[temp_data['Lake']==lake_wanted]
lake_subset.plot(x='date',y='Temp',kind='line',title=f'{lake_wanted}')
plt.tight_layout()
plt.savefig(data_out_directory+f'{lake_wanted}_timeseries.pdf')
print('Done')
