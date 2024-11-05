#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:06:57 2024

@author: evillz
"""

#%% 1. Import pyafmreader loadfile and matplotlib
import matplotlib.pyplot as plt
import pyfmreader_dynamo.src.pyfmreader.pyfmreader as pyfm
# Get documentation about loadfile function
# help(pyfm.loadfile)

#%% Function

def plotTDMSfile (psnex_path, value=None):
    """ Creates a Fcurve plot

    :psnex_path: Either the path to the tdms file to read
        as a string or pathlib.Path, or an already opened file.
    :value: By default plots the raw deflection_channel vs Zposition_sensor

    """
    # Load the PSNEX file
    psnex_file = pyfm.loadfile(psnex_path)
    
    # Get metadata and force curve object
    metadata = psnex_file.filemetadata
    FC = psnex_file.getcurve(0)
    
    # Extract deflection sensitivity and preprocess the force curve
    defl_sens = metadata['defl_sens_nmbyV'] / 1e09  # Convert nm/V to m/V
    FC.preprocess_force_curve(defl_sens, metadata['height_channel_key'])

    
    # Plotting the force curve segments
    plt.figure(figsize=(10, 5))
    

        
    # 8. Get segment 0
    FC_segments = FC.get_segments()
    _, segment_0 = FC_segments[0]
    type(segment_0)  
    
    if value == 1:
        ## Get Force vs Indentation curve
        poc = [6.1, -0.1 *1e-8] # in nm
        spring_k = metadata['spring_const_Nbym']
        FC.get_force_vs_indentation(poc, spring_k)
        
        # plt.figure(figsize=(10,5))
        for segid, segment in FC.get_segments():
            plt.plot(segment.indentation, segment.force, label=f'Segment: {segid}')
        plt.axhline(y=0, color='k', linestyle='--')
        plt.axvline(x=0, color='k', linestyle='--')
        plt.xlabel('Indentation [m]')
        plt.ylabel('Force [N]')
        plt.legend()
        plt.show()
        print("Case 1: Value is 1")
        return

    elif value == 2:
        # 9. Plot only segment 0: approach
        # plt.figure(figsize=(10,5))
        plt.plot(segment_0.zheight, segment_0.vdeflection, label=f'Segment: {segid}')
        plt.xlabel('zheight [nm]')
        plt.ylabel('vdeflection [nm]')
        plt.legend()
        plt.show()
        print("Case 2: Value is 2")
        return 
    elif value == 3:
        # 9. Get force vs indentation for segment 0
        # plt.figure(figsize=(10,5))
        plt.plot(segment_0.indentation, segment_0.force, label=f'Segment: {segid}')
        plt.xlabel('zheight [nm]')
        plt.ylabel('vdeflection [N]')
        plt.legend()
        plt.show()
        print("Case 3: Value is 3")
        return 
    else:
        for segid, segment in FC.get_segments():
            plt.plot(segment.zheight, segment.vdeflection, label=f'Segment: {segid}')
        plt.xlabel('zheight [m]')
        plt.ylabel('vdeflection [m]')
        plt.legend()
        plt.show()
        print ("Default")
        return

   

#%% 2. Load one UFF object with Metadata and Plot
PSNEX_PATH = r'/Users/evillz/Github/PyFMGUI_DyNaMo_tdms/src/pyfmreader_dynamo/tests/PSD__MLCTBIODC_Liq__2024.10.15_16.17.54.88/fcurve_mlctF_cantiA_THp1_Live__2024.10.15_16.26.22.87.tdms'

# PSNEX_FILE = pyfm.loadfile(PSNEX_PATH)


# ## LOAD UFF object into FC
# # type(PSNEX_FILE)
# # metadata = list(PSNEX_FILE.filemetadata.keys())
# metadata = PSNEX_FILE.filemetadata
# FC = PSNEX_FILE.getcurve(0)
# # type (FC)


# defl_sens = metadata['defl_sens_nmbyV'] / 1e09 # nm/V --> m/V
# FC.preprocess_force_curve(defl_sens, metadata['height_channel_key'])

# %%3. Preprocess curve with the deflection sens in the header


# plt.figure(figsize=(10,5))
# for segid, segment in FC.get_segments():
#     plt.plot(segment.zheight, segment.vdeflection, label=f'Segment: {segid}')
# plt.xlabel('zheight [m]')
# plt.ylabel('vdeflection [m]')
# plt.legend()
# plt.show()


# ## Get Force vs Indentation curve
# poc = [6.1, -0.1 *1e-8] # in nm
# spring_k = metadata['spring_const_Nbym']
# FC.get_force_vs_indentation(poc, spring_k)

# plt.figure(figsize=(10,5))
# for segid, segment in FC.get_segments():
#     plt.plot(segment.indentation, segment.force, label=f'Segment: {segid}')
# plt.axhline(y=0, color='k', linestyle='--')
# plt.axvline(x=0, color='k', linestyle='--')
# plt.xlabel('Indentation [m]')
# plt.ylabel('Force [N]')
# plt.legend()
# plt.show()

# # 8. Get segment 0
# FC_segments = FC.get_segments()
# _, segment_0 = FC_segments[0]
# type(segment_0)


# # 9. Plot only segment 0: approach
# plt.figure(figsize=(10,5))
# plt.plot(segment_0.zheight, segment_0.vdeflection, label=f'Segment: 0')
# plt.xlabel('zheight [nm]')
# plt.ylabel('vdeflection [nm]')
# plt.legend()
# plt.show()

# # 9. Get force vs indentation for segment 0
# plt.figure(figsize=(10,5))
# plt.plot(segment_0.indentation, segment_0.force, label=f'Segment: 0')
# plt.xlabel('zheight [nm]')
# plt.ylabel('vdeflection [N]')
# plt.legend()
# plt.show()

#%% Final implementation
plotTDMSfile(PSNEX_PATH)