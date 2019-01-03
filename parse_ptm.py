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
    protid=dataframe[dataframe['percolator q-value'] < 0.05]["protein id"]
    protid.str.split('|').str[1::2].to_csv(targetfilename, index=False)
    print("wrote : " + targetfilename)
    
import glob

for filepath in glob.iglob('./*.psms.sort.txt'):
    pdframe(filepath)

