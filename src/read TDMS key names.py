#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:06:05 2024

@author: evillz
"""

import configparser as confi



config = confi.ConfigParser()
config.read('/Users/evillz/Github/PyFMGUI_DyNaMo_tdms/src/pyfmreader_dynamo/tests/TDMS saving parameters.txt')
sections = list(config.sections())
metadata = {}


for section in sections: 
    # print (f"\033[3m{section}\033[0m")
    for key in config[section]:
        print (section,key, "=", config[section][key])
        metadata[key] = config[section][key]

    print ("----------------------------")
    

    

    

# for sections in 