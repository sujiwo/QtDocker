'''
Created on 21 Feb 2023

@author: sujiwo
'''

from PySide2.QtCore import Slot, QMetaObject, Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from Widgets import *


class CreateContainerWindow(WindowFromUiFile):
    def __init__(self, _parentApp):
        self.parent = _parentApp
        self.gpuWidgetList = []
        WindowFromUiFile.__init__(self, 'createContainer.ui', _parentApp.window)
        self.alreadyTakenLbl.hide()
        self.gpuUsed = []
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
        self.useAllGpuChk.stateChanged.connect(self.useAllGpu)
        
    def fillContents(self):
        self.sourceImageCbx.clear()
        for img in self.parent.imageList:
            self.sourceImageCbx.addItem(img.tags[0])
        self.ramMBInput.setRange(0, self.parent.client.lastInfo['MemTotal']/(1024*1024))
        self.numOfCPUInput.setRange(0, self.parent.client.lastInfo['NCPU'])
        if (len(self.parent.client.gpuList)!=0):
            self.gpuLabel.setEnabled(True)
            self.gpuListScl.setEnabled(True)
            for g in self.parent.client.gpuList:
                chk = QCheckBox(g['name'])
                self.gpuListCtn.layout().addWidget(chk)
                chk.id = g['id']
                self.gpuWidgetList.append(chk)
                chk.stateChanged.connect(lambda x: self.singleGpuChecked(x, chk.id))
                
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
        arg['nano_cpus'] = int(self.numOfCPUInput.value()*1e9)
        arg['mem_limit']=str(self.ramMBInput.value())+'m'
        if self.sharedFolderTblCtn.rowCount()!=0:
            arg['volumes']={}
            for r in range(self.sharedFolderTblCtn.rowCount()):
                p = self.sharedFolderTblCtn.item(r,0).text()
                arg['volumes'][p] = {'bind':self.sharedFolderTblCtn.item(r,1).text(),
                                     'mode':self.sharedFolderTblCtn.item(r,2).text()}
        if self.exitRemoveChk.isChecked()==True:
            arg['auto_remove'] = True
        if len(self.gpuUsed)!=0:
            arg['runtime']='nvidia'
            if self.gpuUsed=='all':
                arg['gpus']='all'
            else:
                pass
            
        return arg
    
    def useAllGpu(self):
        if (self.useAllGpuChk.isChecked()==True):
            print('Using all GPU')
            self.gpuUsed = 'all'
            for w in self.gpuWidgetList:
                w.setEnabled(False)
                w.setChecked(False)
            pass
        else:
            print('Not using any GPU')
            self.gpuUsed = []
            for w in self.gpuWidgetList: 
                w.setEnabled(True)
                w.setChecked(False)
            pass
        
    def singleGpuChecked(self, isChecked, gpuId):
        if (isChecked!=0):
            if gpuId not in self.gpuUsed:
                self.gpuUsed.append(gpuId)
        else:
            if gpuId in self.gpuUsed:
                self.gpuUsed.remove(gpuId)

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
        pathInp.setPlaceholderText("<Host folder or volume name>")
        isReadonlyChk.setText("Read-only")
        modWind.exec_()
    
    
    
    
    
    
        pass