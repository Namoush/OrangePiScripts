# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:06:04 2017

@author: NANDO
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import csv
import skfuzzy as fuzz

## Script da transição do código realizado em matlab para o processsamento e análise
## dos gases presentes da actividade experimental

# Vector representing the time vector of the acquisition (1 -> 12000
# points)
vect_elapsedtime = np.arange(1,12001);

with open('xxxbase.csv', newline='') as csvfile:
    xxxbase = csv.reader(csvfile, delimiter=' ', quotechar='|')
with open('yyybase.csv', newline='') as csvfile:
    yyybase = csv.reader(csvfile, delimiter=' ', quotechar='|')

# Mean of the baseline data acquired
meanBaseTgs = np.mean(xxxbase); meanBaseMics = np.mean(yyybase);

## Introduzir aqui as restantes amostras em formato .csv com a arquitetura semelhante
## ao presente acima


# Agroupar arrays pelo tipo de sensor e pelo tipo de gas

##List of features considered
# List:
# 1 - Mean of the sensor response values;
# 2 - Mean of the slope between each of the consecutive points until the
# 450th point;
# 3 - Mean of the derivatives of the whole response;
# 4 - Stable Value - when the response stabilizes (12000th point - the last
# one acquired);
# 5 - Mean of the differences between the baseline sensor value(ambient
# air) and the response values acquired;
# 6 - Mean differential coefficient value(MDCV);
# 7 - Response Area Value(RAV) - in this case I adapted the function so it
# calculates the area value corresponding to the area from each point in
# the response until an imaginary line at y=1st response point.

# In my opinion, several of these features are somehow redundant and they
# don't enrich the data so much



# Aqui no meio é mais código a chamar funçoes que fazem parte das features que utilizo 
# para fazer feature extraction/engineering. 



# Label the data with the appropriate classification 
# 1 - alcool;
# 2 - vinagre;
arrayLabels = np.array([1,1,1,1,1,2,2,2,2,2]);
       