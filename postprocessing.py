# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:04:03 2017

# PCA/LDA/rLDA(este tenho de fazer à mao se quiser)
# CLustering stuff
# BPNN, KNN, SVM. probably RBFNN, SOM and Recurrent NN


@author: NANDO
"""

import numpy as np
from sklearn.lda import LDA 

def LDA():
    data = np.array();
    #Classification labels
    # array com as labels aqui
    # Setting up LDA characteristics
    clf = LDA();
    clf.fit(data,y);