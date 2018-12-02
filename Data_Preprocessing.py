#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:31:33 2018

@author: echozhao
"""
#%% Data Preprocessing
# Import
import pandas as pd
import numpy as np
from random import sample
from ortools.graph import pywrapgraph

#%%
# Load the data
child_wishlist = pd.read_csv('/Users/echozhao/Documents/2018 Fall/EE 5239/Project/all/child_wishlist_v2.csv', header = None)
gift_goodkids = pd.read_csv('/Users/echozhao/Documents/2018 Fall/EE 5239/Project/all/gift_goodkids_v2.csv', header = None)
child_3 = child_wishlist[0:5001]    # ChildId 0-5000; triplets
child_2 = child_wishlist[5001:45001]   # ChildId 5001-45000; twins
child_1 = child_wishlist[45001:]      # ChildId 45000-999999; single

# Generate random sample  
rindex =  np.array(sample(xrange(len(child_1)), 9549))
child_1_sample = child_1.ix[rindex]
child_2_sample = child_2[0:400]
child_3_sample = child_3[0:51]
child_sample = pd.concat([child_3_sample, child_2_sample, child_1_sample])

#%% Write out data
child_sample.to_csv('/Users/echozhao/Documents/2018 Fall/EE 5239/Project/all/child_sample.csv', index = None)


