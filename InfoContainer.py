'''
Created on 27 Feb 2023

@author: sujiwo
'''

from Widgets import *
import humanize


class InfoContainer(WindowFromUiFile):
    '''
    classdocs
    '''
    def __init__(self, currentContainer, parentApp):
        self.parent = parentApp
        self.container = currentContainer
        WindowFromUiFile.__init__(self, 'infoContainer.ui', parentApp.window)
        self.showAttributes(self.container)
        self.window.setWindowTitle('Statistics for {}'.format(self.container.name))
        
        self.stats = self.container.stats(decode=True)
        next(self.stats)
        self.updateStats()
        
        self.timer = QTimer(self.window)
        self.timer.timeout.connect(self.updateStats)
        self.timer.start(self.parent.config['hz']*1e3)
        
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
        else:
            cpuratio = 0.0
            str_mem_usage = "0B / 0B"
        
        # Real update
        self.cpuUsageDsp.setText("{:.2f}".format(cpuratio)+'%')
        self.memUsageDsp.setText(str_mem_usage)



        