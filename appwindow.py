# This Python file uses the following encoding: utf-8
import sys
import site
import os
import docker
import json
import humanize
from pathlib import Path
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
from MainWindow import Ui_MainWindow
from CreateContainer import CreateContainerWindow
from InfoContainer import InfoContainer
from ImageInfo import ImageInfo
from CommitContainer import CommitContainer
from Host import Host
from Widgets import *


# For Windows, should use %LOCALAPPDATA%/docker.json
configFile = Path(os.environ['HOME']) / '.config' / 'dockerapp.json'
# dir1 = site.get


class WindowFromUiFile(QWidget):
    def __init__(self, uiFilePath, parent):
        super(WindowFromUiFile, self).__init__()
        self.setParent(parent)
        loader = QUiLoader()
        loader.load(uiFilePath, self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        

class DockerApp(QApplication):
    
    def __init__ (self, argv):
        QApplication.__init__(self, argv)
        self.loadConfig()
        
    def _updateContents(self):
        # Update container list
        self.containerList = self.client.getContainerList()
        self.window.containerTableCtn.setRowCount(0)
        self.window.containerTableCtn.setRowCount(len(self.containerList))
        for i in range(len(self.containerList)):
            ctn = self.containerList[i]
            self.window.containerTableCtn.setItem(i, 0, TableItemRO(ctn['ID']))
            self.window.containerTableCtn.setItem(i, 1, TableItemRO(ctn['Name']))
            self.window.containerTableCtn.setItem(i, 2, TableItemRO(ctn['Image']))
            self.window.containerTableCtn.setItem(i, 3, TableItemRO(ctn['CreatedAt']))
            self.window.containerTableCtn.setItem(i, 4, TableItemRO(ctn['State']))
        
        # Update image list
        self.imageList = self.client.getImageList()
        self.window.imageTableCtn.setRowCount(0)
        self.window.imageTableCtn.setRowCount(len(self.imageList))
        for i in range(len(self.imageList)):
            im = self.imageList[i]
            self.window.imageTableCtn.setItem(i, 0, TableItemRO(im['ID']))
            self.window.imageTableCtn.setItem(i, 1, TableItemRO(im['Name']))
            self.window.imageTableCtn.setItem(i, 2, TableItemRO(im['VirtualSize']))
            
        # Update volume list
        
        # Update network list
        self.networkList = self.client.networks.list()
        self.window.networkTableCtn.setRowCount(0)
        self.window.networkTableCtn.setRowCount(len(self.networkList))
        for i in range(len(self.networkList)):
            net = self.networkList[i]
            self.window.networkTableCtn.setItem(i, 0, TableItemRO(net.name))
            self.window.networkTableCtn.setItem(i, 1, TableItemRO(net.attrs['Driver']))
            self.window.networkTableCtn.setItem(i, 2, TableItemRO(net.attrs['Scope']))
            self.window.networkTableCtn.setItem(i, 3, TableItemRO(net.short_id))
            
        # Update system info
        sysInfo = self.client.info()
        displayDictToTree(sysInfo, self.window.sysInfoTree)
        
        
    def createConnection(self):
        self.client = docker.client.DockerClient()
        self._updateContents()
        
    def changeConnection(self):
        url = self.window.hostSelectorBox.lineEdit().text()
        if (url=='Local'): urls = ''
        else: urls = url
        print("Changed: {}".format(urls))
        newclient = Host(urls)
        self.client = newclient
        if url not in self.config['hosts']:
            self.config['hosts'].append(url)
        self._updateContents()
            
    def changeContainerSelection(self, current, prev):
        if (len(current.indexes())!=0):
            selector = current.indexes()[0].row()
            id = self.window.containerTableCtn.item(selector, 0).text()
            self.currentContainer = self.client.containers.get(id)
            if self.currentContainer.status!='running':
                self.window.startContainerBtn.setEnabled(True)
                self.window.stopContainerBtn.setEnabled(False)
                self.window.commitContainerBtn.setEnabled(True)
                self.window.deleteContainerBtn.setEnabled(True)
                self.window.terminalBtn.setEnabled(False)
            elif self.currentContainer.status=='running':
                self.window.startContainerBtn.setEnabled(False)
                self.window.stopContainerBtn.setEnabled(True)
                self.window.commitContainerBtn.setEnabled(False)
                self.window.deleteContainerBtn.setEnabled(False)
                self.window.terminalBtn.setEnabled(True)
            self.window.infoContainerBtn.setEnabled(True)
        else:
            self.window.infoContainerBtn.setEnabled(False)
        
    # XXX: need to change    
    def changeImageSelection(self, current, prev):
        selector = current.indexes()[0].row()
        id = self.window.imageTableCtn.item(selector, 0).text()
        self.currentImage = self.client.images.get(id)
        pass
            
        
    def _setSignals(self):
        self.window.createContainerBtn.clicked.connect(self.createContainerClick)
        self.window.refreshBtn.clicked.connect(self._updateContents)
        self.window.hostSelectorBox.lineEdit().returnPressed.connect(self.changeConnection)
        self.window.hostSelectorBox.currentIndexChanged.connect(self.changeConnection)
        self.window.containerTableCtn.selectionModel().selectionChanged.connect(self.changeContainerSelection)
        self.window.imageTableCtn.selectionModel().selectionChanged.connect(self.changeImageSelection)
        self.window.startContainerBtn.clicked.connect(self.doStartContainer)
        self.window.stopContainerBtn.clicked.connect(self.doStopContainer)
        self.window.deleteContainerBtn.clicked.connect(self.doDeleteContainer)
        self.window.infoContainerBtn.clicked.connect(self.doInspectContainer)
        self.window.inspectBtn.clicked.connect(lambda: ImageInfo(self))
        self.window.commitContainerBtn.clicked.connect(lambda: CommitContainer(self))
        
    def exec_(self):
        self.window = MainWindow()
        self.window.setWindowTitle("QtDocker")
        self.initApp()
        self._setSignals()
        self.window.show()
        # self.createConnection()
        s = QApplication.exec_()
        self.saveConfig()
        return s
    
    # Signal handlers
    def createContainerClick(self):
        # windowNew = WindowFromUiFile('createContainer.ui', self.window)
        # windowNew.show()
        wcreate = CreateContainerWindow(self)
        
        
    def loadConfig(self):
        try:
            fd = open(configFile, mode='r')
            self.config = json.load(fd)
            fd.close()
        except FileNotFoundError:
            # Try to create some configuration
            self.config = {
                'hosts' : ['Local', ],
                'hz' : 1,
            }
    
    def saveConfig(self):
        fd = open(configFile, mode='w')
        json.dump(self.config, fd)
        fd.close()
        
    def initApp(self):
        # Fill with recently succesful connections
        for h in self.config['hosts']:
            self.window.hostSelectorBox.addItem(h)
            
    def doStartContainer(self):
        print('Starting: {}'.format(self.currentContainer.id))
        self.currentContainer.start()
        print('Done')
        
    def doStopContainer(self):
        print('Stopping: {}'.format(self.currentContainer.id))
        self.currentContainer.stop()
        print('Done')
        
    def doInspectContainer(self):
        self.currentContainer.reload()
        InfoContainer(self.currentContainer, self)
        print("Showing tree")

        
    def doDeleteContainer(self):
        ask = QMessageBox()
        ask.setWindowTitle('Confirmation')
        ask.setText('Do you really want to delete \'{}\' ?'.format(self.currentContainer.name))
        ask.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        if (ask.exec_()==QMessageBox.Yes):
            print("Deleting")
            self.currentContainer.remove()
            self._updateContents()
        else: print("Abort deletion")
        


if __name__ == "__main__":
    app = DockerApp(sys.argv)
    s = app.exec_()
    sys.exit(s)
