'''
Created on 21 Feb 2023

@author: sujiwo
'''

from PySide2.QtCore import Slot, QMetaObject, Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from Widgets import *


class WindowFromUiFile():
    def __init__(self, uiFilePath, parentWindow):
        loader = QUiLoader()
        self.window = loader.load(uiFilePath, parentWindow)
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


class CreateContainerWindow(WindowFromUiFile):
    def __init__(self, _parentApp):
        self.parent = _parentApp
        WindowFromUiFile.__init__(self, 'createContainer.ui', _parentApp.window)
        self.window.exec_()
        
    def setupUi(self):
        self._connectSignals()
        self.fillContents()

    def _connectSignals(self):
        # Don't know why we need two lines. connect() directly to method does not work
        self.window.accept = self.performCreate
        self.okBtn.clicked.connect(self.window.accept)
        # Nothing
        self.cancelBtn.clicked.connect(self.window.reject)
        self.addVolBtn.clicked.connect(self.addVolumeClick)
        
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
        if self.numOfCPUInput.value()!=0:
            pass
        return arg

    @Slot()
    def addVolumeClick(self):
        modWind=QDialog()
        modWind.resize(489, 136)
        verticalLayout = QVBoxLayout(modWind)
        verticalLayout.setObjectName("verticalLayout")
        formLayout = QFormLayout()
        formLayout.setObjectName("formLayout")
        formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        formLayout.setWidget(0, QFormLayout.LabelRole, QLabel('Path/Volume:', modWind))
        pathInp = QLineEdit(modWind)
        pathInp.setObjectName("pathInp")
        formLayout.setWidget(0, QFormLayout.FieldRole, pathInp)
        formLayout.setWidget(1, QFormLayout.LabelRole, QLabel("Mount Point:", modWind))
        mountInp = QLineEdit(modWind)
        mountInp.setObjectName("mountInp")
        formLayout.setWidget(1, QFormLayout.FieldRole, mountInp)
        isReadonlyChk = QCheckBox(modWind)
        isReadonlyChk.setObjectName("isReadonlyChk")
        formLayout.setWidget(2, QFormLayout.FieldRole, isReadonlyChk)
        verticalLayout.addLayout(formLayout)
        buttonBox = QDialogButtonBox(modWind)
        buttonBox.setObjectName(u"buttonBox")
        buttonBox.setOrientation(Qt.Horizontal)
        buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        verticalLayout.addWidget(buttonBox)

        def accept():
            res = {'path':pathInp.text(), 'mount':mountInp.text()}
            if isReadonlyChk.isChecked()==True:
                res['access']='ro'
            else: res['access']='rw'
            c = self.sharedFolderTblCtn.rowCount()
            self.sharedFolderTblCtn.setRowCount(c+1)
            self.sharedFolderTblCtn.setItem(c, 0, TableItemRO(res['path']))
            self.sharedFolderTblCtn.setItem(c, 1, TableItemRO(res['mount']))
            self.sharedFolderTblCtn.setItem(c, 2, TableItemRO(res['access']))
            modWind.close()
            pass
        
        buttonBox.accepted.connect(accept)
        buttonBox.rejected.connect(modWind.reject)
        QMetaObject.connectSlotsByName(modWind)
        modWind.setWindowTitle("Add/Edit Container Volume")
        pathInp.setPlaceholderText("<Host Folder>")
        isReadonlyChk.setText("Read-only")
        modWind.exec_()
    
    
    
    
    
    
    
        pass