'''
Created on 27 Feb 2023

@author: sujiwo
'''

from .Widgets import *
import humanize



# XXX: Broken Update !
class ProcessListModel(QAbstractTableModel):
    
    ps_args='-o uid,pcpu,pmem,pid,cmd'
    
    def __init__(self, wparent, container):
        super(ProcessListModel, self).__init__(wparent)
        self.container = container
        self.update()
    
    def update(self):
        if self.container.status!='running':
            return
        # Retrieve list of processes running in this container
        self.lastResult = self.container.top(ps_args=self.ps_args)
        self.dataChanged.emit(self.index(0,0), self.index(-1,-1))

    def columnCount(self, _):
        if self.container.status!='running':
            return 0
        return len(self.lastResult['Titles'])
    
    def rowCount(self, _):
        if self.container.status!='running':
            return 0
        return len(self.lastResult['Processes'])
    
    def data(self, index, role):
        if self.container.status!='running':
            return 0
        if role==Qt.DisplayRole:
            return self.lastResult['Processes'][index.row()][index.column()]
    
    def headerData(self, section, orientation, role):
        if self.container.status!='running':
            return 0
        if role==Qt.DisplayRole:
            if orientation==Qt.Horizontal:
                return self.lastResult['Titles'][section]
            if orientation==Qt.Vertical:
                return str(section+1)


class InfoContainer(WindowFromUiFile):
    '''
    classdocs
    '''
    def __init__(self, currentContainer, parentApp):
        self.wparent = parentApp
        self.container = currentContainer
        WindowFromUiFile.__init__(self, 'infoContainer.ui', parentApp.window)
        self.showAttributes(self.container)
        self.window.setWindowTitle('Statistics for {}'.format(self.container.name))
        
        self.procViewModel = ProcessListModel(self.window, currentContainer)
        self.procView.setModel(self.procViewModel)
        self.procViewModel.dataChanged.connect(self.procView.update)
        
        self.stats = self.container.stats(decode=True)
        next(self.stats)
        self.updateStats()
        
        self.timer = QTimer(self.window)
        self.timer.timeout.connect(self.updateStats)
        self.timer.start(self.wparent.config['hz']*1e3)
        
        self.window.exec_()
        
    def showAttributes(self, container):
        displayDictToTree(container.attrs, self.containerAttrTree)
        
    def updateStats(self):
        # Read next
        gi = next(self.stats)

        if self.container.status=='running':
            # CPU statistics
            cpu_delta = gi['cpu_stats']['cpu_usage']['total_usage'] - gi['precpu_stats']['cpu_usage']['total_usage']
            system_cpu_delta = gi['cpu_stats']['system_cpu_usage'] - gi['precpu_stats']['system_cpu_usage']
            cpuratio = (cpu_delta / system_cpu_delta) * gi['cpu_stats']['online_cpus'] * 100.0
            
            # Memory statistics
            used_memory = gi['memory_stats']['usage'] - gi['memory_stats']['stats']['inactive_file']
            available_memory = gi['memory_stats']['limit']
            str_mem_usage = "{} / {}".format(humanize.naturalsize(used_memory, binary=True), humanize.naturalsize(available_memory, binary=True))
            
            # Processes
            self.notRunningLbl.hide()
            self.updateProcessesView()
        else:
            self.notRunningLbl.show()
            cpuratio = 0.0
            str_mem_usage = "0B / 0B"
        
        # Real update
        self.cpuUsageDsp.setText("{:.2f}".format(cpuratio)+'%')
        self.memUsageDsp.setText(str_mem_usage)
        self.procViewModel.update()

    def updateProcessesView(self):
        pass

        