'''
Created on 21 Feb 2023

@author: sujiwo
'''

import docker
import subprocess
import re
import xml.dom.minidom


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
                uuid=matches[3]
                self.gpuList.append({'id':gpuid, 'name':gpuname, 'uuid':uuid})
            return True
        except:
            return False
    
    def hasNvidiaContainerSupport(self):
        pass
    
    # Parse more complete output of nvidia-smi with XML
    # XXX: Unfinished
    def hasGpu2(self):
        self.gpuList = []
        try:
            if self.remote==False:
                cmdoutput = subprocess.run(['nvidia-smi', '-q', '-x'], capture_output=True)
            else:
                stdin, stdout, stderr = self.ssh_client.exec_command('nvidia-smi -q -x')
                cmdoutput = stdout.read()
            return True
        except:
            return False
            
    
    # XXX: Need to fix
    def getContainerList(self):
        return self.containers.list(all=True, sparse=True)
    
    def getImageList(self):
        return self.images.list()
    

        