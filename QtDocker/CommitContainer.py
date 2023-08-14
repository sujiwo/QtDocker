'''
Created on 1 Mar 2023

@author: sujiwo
'''

from .Widgets import *


class CommitContainer(WindowFromUiFile):

    def __init__(self, parentApp):
        self.wparent = parentApp
        WindowFromUiFile.__init__(self, 'commitContainer.ui', parentApp.window)
        self.window.exec_()
        
    def setupUi(self):
        self.window.setWindowTitle('Commit Container')
        self.window.accepted.connect(self.doCommit)
        
    def doCommit(self):
        print('Committing')
        # self.wparent.currentContainer.
        pass