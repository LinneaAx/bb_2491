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
    protidq=dataframe[dataframe['percolator q-value'] < 0.05]["protein id"]
    qfiltered=dataframe[dataframe['percolator q-value'] < 0.05]
    withmodification=qfiltered['sequence'].str.contains("79.97")
    filteredmodified=qfiltered[withmodification]
    
    #modifications = filteredmodified['sequence'].str.split("[\[\]]").str[1::2]
    y = filteredmodified['sequence'].str.contains('Y\[7')
    t = filteredmodified['sequence'].str.contains('T\[7')
    s = filteredmodified['sequence'].str.contains('S\[7')
    
    ylist = filteredmodified[y]
    yprotid = ylist["protein id"].str.split('|').str[1].str.split('-').str[0]
    y1 = yprotid + '-Y'
    y2 = pd.concat([yprotid, y1], axis=1)
    y2['mod']='Y'
    
    tlist = filteredmodified[t]
    tprotid = tlist["protein id"].str.split('|').str[1].str.split('-').str[0]
    t1 = tprotid + '-T'
    t2 = pd.concat([tprotid, t1], axis=1)
    t2['mod']='T'
    
    slist = filteredmodified[s]
    sprotid = slist["protein id"].str.split('|').str[1].str.split('-').str[0]
    s1 = sprotid + '-S'
    s2 = pd.concat([sprotid, s1], axis=1)
    s2['mod']='S'
    
    merged = pd.concat([y2,t2,s2], axis=0)
    
    #targetfilename = target_psms[:-4] + "merged.79.97.filter-0.05.txt"
    targetfilename = 'parsed25-37'
    with open(targetfilename, 'a') as f:
        merged.to_csv(f, header=False, index=False)

    print("wrote : " + target_psms)
    
#pdframe('percolator.target.psms.sort.txt')

import glob

for filepath in glob.iglob('./*IPG2*.psms.sort.txt'):
   pdframe(filepath)