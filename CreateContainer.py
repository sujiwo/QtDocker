'''
Created on 21 Feb 2023

@author: sujiwo
'''

from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader


class WindowFromUiFile():
    def __init__(self, uiFilePath, parentWindow):
        loader = QUiLoader()
        self.window = loader.load(uiFilePath, parentWindow)
        self.childList = {}
        self.enumChildrenTree(self.window)
        
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


class CreateContainerWindow(WindowFromUiFile):
    def __init__(self, _parentApp):
        WindowFromUiFile.__init__(self, 'createContainer.ui', _parentApp.window)
        self.parent = _parentApp
        self._connectSignals()
        self.fillContents()
        self.show()

    def _connectSignals(self):
        # Don't know why we need two lines. connect() directly to method does not work
        self.window.accept = self.performCreate
        self.okBtn.clicked.connect(self.window.accept)
        # Nothing
        self.cancelBtn.clicked.connect(self.window.reject)
        
    def fillContents(self):
        self.sourceImageCbx.clear()
        for img in self.parent.imageList:
            self.sourceImageCbx.addItem(img.tags[0])
        self.ramGBInput.setRange(0, self.parent.client.lastInfo['MemTotal']/(1024*1024))
        self.numOfCPUInput.setRange(0, self.parent.client.lastInfo['NCPU'])
        if (len(self.parent.client.gpuList)!=0):
            self.gpuLabel.setEnabled(True)
            self.gpuListScl.setEnabled(True)
            for g in self.parent.client.gpuList:
                chk = QCheckBox(g['name'])
                self.gpuListCtn.layout().addWidget(chk)
                chk.id = g['id']
                
    def performCreate(self):
        print('Validating...')
        containerArg = self._makeContainerArg()
        self.parent.client.containers.create(**containerArg)
        self.window.close()
        self.parent._updateContents()
    
    def _makeContainerArg(self):
        arg = {}
        arg['name'] = self.nameInput.text()
        arg['image'] = self.sourceImageCbx.currentText()
        if (self.isInteractive.isChecked()==True):
            arg['stdin_open']=True
            arg['tty']=True
        return arg

    
    
    
    
    
    
    
    
        pass