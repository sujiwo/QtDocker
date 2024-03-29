'''
Created on 21 Feb 2023

@author: sujiwo
'''

from PySide2.QtCore import Slot, QMetaObject, Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from .Widgets import *
from docker.types import DeviceRequest


class CreateContainerWindow(WindowFromUiFile):
    def __init__(self, _parentApp):
        self.wparent = _parentApp
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
        for img in self.wparent.imageList:
            self.sourceImageCbx.addItem(img['Name'])
        self.ramMBInput.setRange(0, self.wparent.client.lastInfo['MemTotal']/(1024*1024))
        self.numOfCPUInput.setRange(0, self.wparent.client.lastInfo['NCPU'])
        if (len(self.wparent.client.gpuList)!=0):
            self.gpuLabel.setEnabled(True)
            self.gpuListScl.setEnabled(True)
            for g in self.wparent.client.gpuList:
                chk = QCheckBox(g['name'])
                self.gpuListCtn.layout().addWidget(chk)
                chk.id = g['id']
                self.gpuWidgetList.append(chk)
                chk.stateChanged.connect(lambda x: self.singleGpuChecked(x, chk.id))
                
    def performCreate(self):
        print('Validating...')
        containerArg = self._makeContainerArg()
        self.wparent.client.containers.create(**containerArg)
        self.window.close()
        self.wparent._updateContents()
    
    def _makeContainerArg(self):
        arg = {}
        arg['devices'] = []
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
            capabilities=[['compute','utility','graphics','video','display']]
            if self.gpuUsed=='all':
                arg['device_requests']=[DeviceRequest(count=-1, driver='nvidia', capabilities=capabilities)]
            else:
                devId = [self.wparent.client.gpuList[g]['uuid'] for g in self.gpuUsed]
                arg['device_requests']=[DeviceRequest(device_ids=devId, driver='nvidia', capabilities=capabilities)]

        ports={}
        for r in range(self.portmapTbl.rowCount()):
            try:
                src=self.portmapTbl.item(r,0).text()
            except AttributeError: continue
            if len(src)!=0:
                try: 
                    dst=self.portmapTbl.item(r,1).text()
                except AttributeError: 
                    dst = None
                ports[src]=dst
        arg['ports']=ports
        
        match self.restartPolCbx.currentText():
            case 'On failure, retry 3 times':
                arg['restart_policy'] = {'Name': 'on-failure', 'MaximumRetryCount':3}
            case 'Always':
                arg['restart_policy'] = {'Name': 'always'}
            case 'Unless stopped':
                arg['restart_policy'] = {'Name': 'unless-stopped'}
                
        if self.serialPortChk.isChecked()==True:
            serialPort = self.serialPortChooser.currentText()
            arg['devices'].append('{}:{}:rwm'.format(serialPort, serialPort))
            
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