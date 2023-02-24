'''
Created on 21 Feb 2023

@author: sujiwo
'''

import docker
import subprocess
import re

nvidia_smi_re = '^GPU ([0-9]+): ([\-\s\w]+) \(UUID: ([\-0-9A-Za-z]+)\)'


class Host(docker.DockerClient):
    '''
    classdocs
    '''

    def __init__(self, url):
        docker.DockerClient.__init__(self, base_url=url)
        if (url.startswith('ssh')):
            self.remote = True
            self.ssh_client = self.api._custom_adapter.ssh_client
        else: self.remote = False
        self.lastInfo = self.info()
        x = self.hasGpu()
        pass
    
    def getInfo(self):
        pass
    
    def hasGpu(self):
        self.gpuList = []
        try:
            if self.remote==False:
                cmdoutput = subprocess.run(['nvidia-smi', '-L'], capture_output=True)
                gpul = cmdoutput.stdout.decode('utf-8').strip().splitlines()
            else:
                stdin, stdout, stderr = self.ssh_client.exec_command('nvidia-smi -L')
                gpul = stdout.readlines()
            for g in gpul:
                matches=re.match(nvidia_smi_re, g)
                gpuid=int(matches[1])
                gpuname=matches[2]
                gpuuuid=matches[3]
                self.gpuList.append({'id':gpuid, 'name':gpuname, 'uuid':gpuuuid})
            return True
        except:
            return False
    
    def getImageList(self):
        pass
    
    def getContainerList(self):
        pass
    
    def hasNvidiaContainerSupport(self):
        
        pass
    
    