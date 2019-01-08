# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:32:50 2019

@author: Linnea
"""

import pandas as pd
import sys
import matplotlib 
import re
import numpy as np
import matplotlib.pyplot as plt
import os

def pdframe(target_psms):
    
    dataframe = pd.read_table(target_psms)
    targetfilename = target_psms[:-4] + ".filter-0.05.txt"
    qfiltered=dataframe[dataframe['percolator q-value'] < 0.05]

    protids = qfiltered["protein id"].str.split('|').str[1].str.split('-').str[0]

    targetfilename = 'parsed_allproteins3-10'
    with open(targetfilename, 'a') as f:
        protids.to_csv(f, header=False, index=False)

    print("wrote : " + target_psms)
    
import glob

for filepath in glob.iglob('./*IPG3*.psms.sort.txt'):
   pdframe(filepath)