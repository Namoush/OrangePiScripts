# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:14:38 2017

@author: NANDO
"""

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Simple')
wid.show()

sys.exit(app.exec_())