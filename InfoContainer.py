'''
Created on 27 Feb 2023

@author: sujiwo
'''

from Widgets import *


class InfoContainer(WindowFromUiFile):
    '''
    classdocs
    '''


    def __init__(self, currentContainer, parentApp):
        self.parent = parentApp
        self.container = currentContainer
        WindowFromUiFile.__init__(self, 'infoContainer.ui', parentApp.window)
        self.updateStat(self.container)
        self.window.setWindowTitle('Statistics for {}'.format(self.container.name))
        self.window.exec_()
        
    def updateStat(self, container):
        displayDictToTree(container.attrs, self.containerAttrTree)