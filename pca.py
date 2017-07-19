# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:27:11 2017

@author: NANDO
"""
import numpy as np
from sklearn.decomposition import PCA

def princ_component():
    data = np.array();
    # Setting up PCA characteristics
    pca = PCA(n_components=2);  
    pca.fit(data);
    



    

    