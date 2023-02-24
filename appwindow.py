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
from Host import Host



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
        

class tableItemRO(QTableWidgetItem):
    def __init__(self, text):
        QTableWidgetItem.__init__(self, text)
        # self.setFlags(self.flags() & ~Qt.ItemIsEditable & Qt.ItemIsSelectable & Qt.ItemIsEnabled)


class DockerApp(QApplication):
    
    def __init__ (self, argv):
        QApplication.__init__(self, argv)
        self.loadConfig()
        
    def _updateContents(self):
        # Update container list
        self.containerList = self.client.containers.list(all=True, sparse=True)
        self.window.containerTableCtn.setRowCount(0)
        self.window.containerTableCtn.setRowCount(len(self.containerList))
        for i in range(len(self.containerList)):
            ctn = self.containerList[i]
            self.window.containerTableCtn.setItem(i, 0, tableItemRO(ctn.name))
            self.window.containerTableCtn.setItem(i, 1, tableItemRO(ctn.image.tags[0]))
            self.window.containerTableCtn.setItem(i, 3, tableItemRO(ctn.status))
            self.window.containerTableCtn.setItem(i, 4, tableItemRO(ctn.id[0:12]))
        
        # Update image list
        self.imageList = self.client.images.list()
        self.window.imageTableCtn.setRowCount(0)
        self.window.imageTableCtn.setRowCount(len(self.imageList))
        for i in range(len(self.imageList)):
            im = self.imageList[i]
            self.window.imageTableCtn.setItem(i, 0, tableItemRO(im.tags[0]))
            size = humanize.naturalsize(im.attrs['Size'])
            self.window.imageTableCtn.setItem(i, 1, tableItemRO(size))
            
        # Update volume list
        
        # Update network list
        self.networkList = self.client.networks.list()
        self.window.networkTableCtn.setRowCount(0)
        self.window.networkTableCtn.setRowCount(len(self.networkList))
        for i in range(len(self.networkList)):
            net = self.networkList[i]
            self.window.networkTableCtn.setItem(i, 0, tableItemRO(net.name))
            self.window.networkTableCtn.setItem(i, 1, tableItemRO(net.attrs['Driver']))
            self.window.networkTableCtn.setItem(i, 2, tableItemRO(net.attrs['Scope']))
            self.window.networkTableCtn.setItem(i, 3, tableItemRO(net.short_id))
        
    def createConnection(self):
        self.client = docker.client.DockerClient()
        self._updateContents()
        
    def changeConnection(self):
        url = self.window.hostSelectorBox.lineEdit().text()
        if (url=='Local'): urls = ''
        else: urls = url
        print("Changed: {}".format(urls))
        try:
            newclient = Host(urls)
            self.client = newclient
            if url not in self.config['hosts']:
                self.config['hosts'].append(url)
            self._updateContents()
        except Exception as e:
            print('Unable to connect: {}'.format(e.args))
            
    def changeContainerSelection(self, current, prev):
        if (len(current.indexes())!=0):
            selector = current.indexes()[0].row()
            container = self.containerList[selector]
            if container.status=='exited':
                self.window.startContainerBtn.setEnabled(True)
                self.window.stopContainerBtn.setEnabled(False)
                self.window.commitContainerBtn.setEnabled(True)
                self.window.deleteContainerBtn.setEnabled(True)
                self.window.terminalBtn.setEnabled(False)
            elif container.status=='running':
                self.window.startContainerBtn.setEnabled(False)
                self.window.stopContainerBtn.setEnabled(True)
                self.window.commitContainerBtn.setEnabled(False)
                self.window.deleteContainerBtn.setEnabled(False)
                self.window.terminalBtn.setEnabled(True)
            self.window.infoContainerBtn.setEnabled(True)
        else:
            self.window.infoContainerBtn.setEnabled(False)
            
        
    def _setSignals(self):
        self.window.createContainerBtn.clicked.connect(self.createContainerClick)
        self.window.refreshBtn.clicked.connect(self._updateContents)
        self.window.hostSelectorBox.lineEdit().returnPressed.connect(self.changeConnection)
        self.window.hostSelectorBox.currentIndexChanged.connect(self.changeConnection)
        self.window.containerTableCtn.selectionModel().selectionChanged.connect(self.changeContainerSelection)
        
    def exec_(self):
        self.window = MainWindow()
        self.window.setWindowTitle("DockerApp")
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
                'hosts' : ['Local', ]
            }
    
    def saveConfig(self):
        fd = open(configFile, mode='w')
        json.dump(self.config, fd)
        fd.close()
        
    def initApp(self):
        # Fill with recently succesful connections
        for h in self.config['hosts']:
            self.window.hostSelectorBox.addItem(h)


if __name__ == "__main__":
    app = DockerApp(sys.argv)
    s = app.exec_()
    sys.exit(s)