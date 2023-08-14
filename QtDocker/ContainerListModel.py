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
    columns = ['ID', 'Name', 'Image', 'Created', 'Status']

    def __init__(self, wparent):
        self.wparent = wparent
        super(ContainerListModel, self).__init__(wparent)
        try:
            self.filteredList = self.wparent.containerList
        except AttributeError: self.filteredList = None
        
    def filterChanged(self):
        self.filteredList = self.matchContainers(self.wparent.window.containerFilterInp.text())
        
    def matchContainers(self, query):
        cmatches = []
        for c in self.wparent.containerList:
            stringMatches = c['ID']+c['Name']+c['Image']+c['State']
            if re.search(query, stringMatches):
                cmatches.append(c['Name'])
        return cmatches

    def columnCount(self, _)->int:
        return len(self.columns)
    
    def rowCount(self, _)->int:
        if self.filteredList is None: return 0
        return len(self.filteredList)
    
    def data(self, index, role):
        if role==Qt.DisplayRole:
            field = self.columns[index.column()]
            return self.filteredList[index.row()][field]
    
    def headerData(self, section, orientation, role):
        if role==Qt.DisplayRole:
            if orientation==Qt.Horizontal:
                self.columns[section]
            if orientation==Qt.Vertical:
                return str(section+1)