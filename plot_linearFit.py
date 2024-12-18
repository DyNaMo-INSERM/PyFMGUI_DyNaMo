#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:56:28 2024

@author: evillz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Example data
x = np.linspace(0, 10, 100)  # Independent variable
y = 3 * x + 5 + np.random.normal(0, 2, size=len(x))  # Linear data with noise

# Define the region of interest (e.g., 4 <= x <= 8)
region_mask = (x >= 4) & (x <= 8)
x_region = x[region_mask]
y_region = y[region_mask]

# Perform linear regression (slope fit) on the defined region
slope, intercept, r_value, p_value, std_err = linregress(x_region, y_region)

# Calculate the fitted line for the region
fitted_line = slope * x_region + intercept

# Plot the original data and the fit
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Original Data', color='blue', alpha=0.6)
plt.plot(x_region, fitted_line, label=f'Fit: y = {slope:.2f}x + {intercept:.2f}', color='red', linestyle='--')
plt.axvspan(4, 8, color='yellow', alpha=0.2, label='Fitting Region')
plt.title('Linear Slope Fit for a Defined Region')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()