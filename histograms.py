# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:28:23 2019

@author: User
"""

import pandas as pd
flights = pd.read_csv('data/formatted_flights.csv')
flights.head(10) #output the first 10 flights delay

#import the libraries
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib histogram
plt.hist(flights['arr_delay'], color='blue', edgecolor='black',
         bins = int(180/5))

#seaborn histogram
sns.distplot(flights['arr_delay'], hist=True, kde=False,
             bins = int(180/5), color ='blue',
             hist_kws={'edgecolor':'black'})
#add labels
plt.title('Histogram of Arrival Delays)
plt.xlabel('Delay (min)')