#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:53:36 2024

@author: evillz
"""

import os
# from pyfmreader_dynamo.src.pyfmreader.constants.py import *
import pyfmreader_dynamo.src.pyfmreader.pyfmreader as pyfm
from OpenTDMSFile import plotTDMSfile

# Define the directory path
directory_path = '/Users/evillz/Data/psnex_map___2024.10.15_17.13.55.20'
# Loop through all files in the directory
filepaths = os.listdir(directory_path)

tdms_files = []
for filename in filepaths:
    # Check if the file has a .tdms extension
    if filename.endswith(pyfm.psnexfiles):
        tdms_files += [filename]
        
for tdmsFile in tdms_files[:20]:
    # Full file path
    file_path = os.path.join(directory_path, tdmsFile)
    # print(f"Processing file: {file_path}")
    print(tdmsFile[:-5] )
    plotTDMSfile(file_path)
        
        
        # Add your code to process the .tdms file here