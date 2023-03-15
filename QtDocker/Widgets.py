'''
Created on 25 Feb 2023

@author: sujiwo
'''


from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from pathlib import Path
import os


myUiPath = Path(os.path.dirname(__file__))


class TableItemRO(QTableWidgetItem):
    def __init__(self, text):
        QTableWidgetItem.__init__(self, text)


class WindowFromUiFile():
    def __init__(self, uiFilePath, parentWindow):
        loader = QUiLoader()
        if os.path.isabs(uiFilePath)==False:
            uiFilePath = myUiPath / 'ui' / uiFilePath
        self.window = loader.load(str(uiFilePath), parentWindow)
        self.childList = {}
        self.enumChildrenTree(self.window)
        self.setupUi()
        
    def show(self):
        self.window.show()
        
    def w(self, objectName):
        try:
            return self.childList[objectName]
        except KeyError:
            return None
        
    def __getattr__(self, objectName):
        try:
            return self.childList[objectName]
        except KeyError:
            raise AttributeError("Object {} not found".format(objectName))
        
    def enumChildrenTree(self, parent):
        for o in parent.children():
            if o.objectName()=='':
                continue
            if len(o.children())!=0 :
                self.enumChildrenTree(o)
            else: pass
            self.childList[o.objectName()] = o
        return
    
    def setupUi(self):
        pass


def displayDictToTree(sourcedict, tree):
    def _createTreeItem(k, v, parent):
        ix = QTreeWidgetItem(parent)
        ix.setText(0, str(k))
        if (type(v)==dict):
            for kc in v:
                _createTreeItem(kc, v[kc], ix)
        elif (type(v)==list):
            for i in range(len(v)):
                _createTreeItem(i, v[i], ix)
        else:
            ix.setText(1, str(v))
    # Cleanup
    tree.clear()
    for k in sourcedict:
        _createTreeItem(k, sourcedict[k], tree)
        

