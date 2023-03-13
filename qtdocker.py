#!/usr/bin/python3

'''
Created on 13 Mar 2023

@author: sujiwo
'''

import sys
from QtDocker import QtDocker

if __name__=="__main__":
    app = QtDocker(sys.argv)
    s = app.exec_()
    sys.exit(s)