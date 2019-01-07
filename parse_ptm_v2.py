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
    withmodification=qfiltered['sequence'].str.contains("\[")
    filteredmodified=qfiltered[withmodification]
    modifications = filteredmodified['sequence'].str.split("[\[\]]").str[1::2]
    protid = filteredmodified["protein id"].str.split('|').str[1]
    modprot = pd.concat([modifications,protid],axis=1)
    
    firstmodfilter = modprot['sequence'].apply(''.join).str.contains('15.99')
    secondmodfilter = modprot['sequence'].apply(''.join).str.contains('79.97')
    
    targetfilename = target_psms[:-4] + ".15.99.filter-0.05.txt"
    modprot[firstmodfilter]['protein id'].to_csv(targetfilename, index=False)
    
    print("wrote : " + targetfilename)
    
    targetfilename = target_psms[:-4] + ".79.97.filter-0.05.txt"
    modprot[secondmodfilter]['protein id'].to_csv(targetfilename, index=False)
    
    print("wrote : " + targetfilename)
    
import glob

for filepath in glob.iglob('./*.peptides.sort.txt'):
    pdframe(filepath)