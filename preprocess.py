# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:00:20 2017

In this script, I plan to implement the different methods for pre processing the
sensor data.
Each method will be a feature for the 4 sensors chosen.

# 1 - Mean of the sensor response values;
# 3 - Mean of the derivatives of the whole response;
# 4 - Stable Value - when the response stabilizes (before the purging phase);
# 5 - Mean of the differences between the baseline sensor value(ambient
# air) and the response values acquired;
# 6 - Mean differential coefficient value(MDCV);
# 7 - Response Area Value(RAV) - in this case I adapted the function so it
# calculates the area value corresponding to the area from each point in
# the response until an imaginary line at y=1st response point.
# 8 - FFT
# 9 - DWT
# 10 - Moving Window Time Slice


@author: NANDO
"""
import numpy as np
import matplotlib as mpl
import pywt
import scipy as sci
#import pywt

def mean (data):
    # Mean of the data prompted when calling this function
    cenas = np.array(data);
    mean_data = np.mean(cenas);
    return mean_data
    
def slope_mean():
    # Mean of the data points contained in the slope when the sensor response
# kicks in. Probably it is redundant 
    # Selection of the data points to consider
    data_slope = np.array(x-y);
    mean_slope = np.mean(data_slope);
    
    return mean_slope
    
def derivatives_mean(data):
    # Mean of the derivatives of each data point 
    data = np.array();
    dx=1;
    dy = diff(data)/dx;
    mean_deriv = np.mean(dy);
    return mean_deriv
    
def rsp_area_value(data):
    # Area under the response value. From 0 to each point of the response
    data = np.array();
    minimum = min(data);
    
    # return resp_area

def diff_baseline(data, database):
    data = np.array();
    database = np.array();
    
    diff_b = np.subtract(database-data);
    # I might need to eventually solve negative values, not sure
    
    return diff_b
    
    #Numpy or Scipy implementation
def fourier_transform(data):
    # Application of the Fast Fourier Transform (we get the frequency spectrum
    # discretized)
    coeffs = fft(data);
    return coeffs

def wavelet_transform():
    
    # Easy configuration. Check PyWavelets documentation
    # cA - approximation coefficients
    # cD - details coefficients
    
    # Apparently, db and bior are the most suitable for this problem according to 
    # an article I read. Probably I should use several to see which ones are the best
    # for this case
    cA, cD = pywt.dwt([data, 'db1']);
    
    return cA, cD
                     
def windowTimeSlicing():
    
    # This method is very similar to the response area calculation
    # Don't know yet if it is worth to use it
    
    # First I need to define the bell shaped function in order to "create" four
    #bell shaped curves alongside our acquisitions 
    
    # Each bell function will have one fourth of the points of each sample as width. 
    
    
    
    
    