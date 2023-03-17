'''
Created on 17 Mar 2023

@author: sujiwo
'''

import re
from .Widgets import *


class ContainerListModel(QAbstractTableModel):
    '''
    classdocs
    '''

    def __init__(self, parent):
        self.parent = parent
        super(ContainerListModel, self.__init__(parent))
        
    def filterChanged(self):
        pass
        
    def matchContainers(self, query):
        cmatches = []
        for c in self.parent.containerList:
            stringMatches = c['ID']+c['Name']+c['Image']+c['State']
            if re.search(query, stringMatches):
                cmatches.append(c['Name'])
        print(cmatches)
        return cmatches

    def columnCount(self, _)->int:
        pass
    
    def rowCount(self, _)->int:
        pass
    
    def data(self, index, role):
        pass
    
    def headerData(self, section, orientation, role):
        pass